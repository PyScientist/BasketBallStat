import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsRegressor
from StatSmart_app import perform_single_team_analysis, DataForPrediction


fontdict_title = {'fontsize': 10,
                  'fontweight': 20,
                  'color': 'black',
                  'verticalalignment': 'baseline',
                  'horizontalalignment': 'center'}


fontdict_axes = {'fontsize': 10,
                 'fontweight': 20,
                 'color': 'black',
                 'verticalalignment': 'baseline',
                 'horizontalalignment': 'center'}


def add_grid(axes):
    axes.grid(color='grey', linestyle='-', linewidth=0.5, which='major', axis='both')
    axes.grid(color='lightblue', linestyle='-', linewidth=0.5, which='minor', axis='both')
    axes.minorticks_on()


def plot_equal_values_line(ax, x_min=0, x_max=10000, quantity=10000, color='grey'):
    x = np.linspace(x_min, x_max, quantity)
    return ax.plot(x, x, c=color, linestyle='--', label='Line of equal values')


def plot_error_percent_lines(ax, x_min=0, x_max=10000, quantity=10000, color='grey', percentage=10):
    x = np.linspace(x_min, x_max, quantity)
    y1 = x - x * percentage / 100
    y2 = x + x * percentage / 100
    return (ax.plot(x, y1, c=color, linestyle='--', label=F'Error -{percentage}%'),
            ax.plot(x, y2, c=color, linestyle='--', label=F'Error +{percentage}%'))


def prepare_data_for_prediction(target, league, team, op_team, home_flag,
                                next_play_date, days_for_model, days_for_param):
    return {
        'target': target,
        'league': league,
        'team': team,
        'op_team': op_team,
        'home_flag': home_flag,
        'next_play_date': next_play_date,
        'time_frames_model': (0, days_for_model),
        'time_frames_median_model': (0, days_for_param),
        }


def make_prediction(df, pa: dict) -> dict:
    """
    :param df: dataframe to analysis
    :param pa: prediction assignment
    :return: predicted value
    """
    sta = perform_single_team_analysis(team=pa['team'],
                                       df_main=df,
                                       next_play_date=pa['next_play_date'],
                                       time_frames=pa['time_frames_model'])

    Model = AbstractBasketballModel(sta)
    Model.set_target(pa['target'])
    Model.get_features(mode='standard')
    Model.train_model_knr(k=3)

    dfp = DataForPrediction(df_main=df,
                            team=pa['team'],
                            op_team=pa['op_team'],
                            home_flag=pa['home_flag'],
                            next_play_date=pa['next_play_date'],
                            time_frames=pa['time_frames_median_model'])

    y_calc = Model.make_prediction_knr(input_params=dfp.data_for_prediction)

    return {'y_calc': y_calc, 'dfp': dfp, 'model': Model}


class AbstractBasketballModel:

    def __init__(self, single_team_analysis):
        """
        При инициализации модели возможно задать на сколько давно были игры относительно прогнозируемой, если
        прогноз осуществляется в ретроспективе все положительные приращения должны быть отброшены
        давность игр определяется посредством поля TimeShift дата фрейма df.
        """

        self.df = single_team_analysis['df']  # дата фрейм для обучения по команде
        self.team = single_team_analysis['t_name']  # название команды
        self.c_matrix = single_team_analysis['c_matrix']  # корреляционная матрица по команде
        self.targets = single_team_analysis['targets']  # список выявленных целевых параметров в наборе данных
        self.targets.remove('Victory flag')  # удаляем цели которые пока не поддерживаются
        self.params = single_team_analysis['params']  # список выявленных фитчей в наборе данных
        self.features = []
        self.target = None
        self.meaning_correlatives = None
        self.X = None
        self.y = None
        self.sc = None

        self.model_knr = None
        self.model_lr = None
        self.packed_knr_results_calc = None

    def add_meaning_params(self):
        list_to_add = ['FT% #1', 'FTA #1', 'FT% #2', 'FTA #2']
        list_to_add = []
        for param in list_to_add:
            if param in self.features:
                pass
            else:
                self.features.append(param)

    def set_target(self, target) -> None:
        if target in self.targets:
            self.target = target
        else:
            print(f'There is no such target "{target}" in targets: "{self.targets}"\nPlease choose another one!')

    def get_features(self, mode='standard') -> None:

        target_corr = self.c_matrix.loc[:, ([self.target])]  # Получаем коэффициенты корреляции для целевого параметра

        # Задаем диапазоны коэффициентов корреляции, которые будем считать значимыми
        target_corr[f'{self.target}_correlation_degree'] = pd.cut(target_corr[self.target],
                                                                  [-1, -0.9, -0.7, -0.5, -0.35, -0.1, 0.1, 0.35, 0.5,
                                                                   0.7, 0.9, 1],
                                                                  labels=["very high negative", "high negative",
                                                                          "notable negative", "moderate negative",
                                                                          "weak negative",
                                                                          "absence", "weak", "moderate", "notable",
                                                                          "high", "very high"])

        if mode == 'standard':
            selection = ["very high negative", "high negative", "notable negative",
                         "moderate negative", "moderate", "notable", "high", "very high"]
        elif mode == 'precise':
            selection = ["very high negative", "high negative", "notable negative",
                         "notable", "high", "very high"]
        else:
            selection = ["very high negative", "high negative", "notable negative",
                         "notable", "high", "very high"]
            print('please choose correct mode "standard" or "precise"')

        '''Отберем параметры, оставив только те, где имеется значимые коэффициенты корреляции
        Получим значение и величину корреляции'''
        self.meaning_correlatives = target_corr[target_corr[f'{self.target}_correlation_degree'].isin(selection)]
        # Получим список самих параметров
        self.features = list(self.meaning_correlatives.index)

        # Удалим флаг победы как фитчу на которую стоит ориентироваться (если она добавлена)
        if 'Victory flag' in self.features:
            self.features.remove('Victory flag')

        # Проверим корректность подбора фичей
        for feature in self.features:
            if feature not in self.params:
                print(f'The chosen feature "{feature}" is not exist in dataframe, please check the data')

        self.add_meaning_params()

    def train_model_knr(self, k) -> None:
        self.X = self.df[self.features].values  # готовим обучающую выборку по фичам
        self.y = self.df[self.target].values  # готовим обучающую выборку по целям
        # Делим дата сет на обучающий и тестовый
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, random_state=101, test_size=.1)

        # Проводим масштабирование данных
        self.sc = MinMaxScaler()
        self.sc.fit_transform(X_train)
        X_train_scaled = self.sc.transform(X_train)
        X_test_scaled = self.sc.transform(X_test)

        # Инициализируем и обучаем модель
        self.model_knr = KNeighborsRegressor(n_neighbors=k)
        self.model_knr.fit(X_train_scaled, y_train)

        # оцениваем модель
        self.packed_knr_results_calc = [y_train, self.model_knr.predict(X_train_scaled),
                                        y_test, self.model_knr.predict(X_test_scaled)]

    def make_prediction_knr(self, input_params) -> None:
        """Осуществляем прогноз по модели и наносим на график результаты прогноза"""
        # Масштабируем данные
        X_scaled = self.sc.transform(list(input_params[self.features].values))
        # Осуществляем прогноз
        return self.model_knr.predict(X_scaled)[0]

    def plot_knr_training_results(self, ax) -> None:

        def prepare_pairs_parameter_correlations(self):
            correlation_series = self.c_matrix.loc[:, ([self.target])]

            correlation_pairs = [[feature,
                                  round(float(correlation_series.loc[[feature]].values[0][0]), 2)] for feature in self.features]

            correlation_strings = 'Features for prediction:'
            for i,item in enumerate(correlation_pairs):
                correlation_strings += f'{i+1}) {item[0]} R = {item[1]};\n'

            return correlation_strings

        correlation_pairs = prepare_pairs_parameter_correlations(self)
        print(correlation_pairs)

        ax.clear()
        y_train, y_train_calc, y_test, y_test_calc = self.packed_knr_results_calc
        ax.set_title(f'KNR Model for {self.target}, team {self.team}')
        plot_equal_values_line(ax)
        plot_error_percent_lines(ax, percentage=5, color='lavender')
        plot_error_percent_lines(ax, percentage=10, color='coral')
        ax.scatter(y_train, y_train_calc, label='train selection', color='red')
        ax.scatter(y_test, y_test_calc, label='test selection', color='green')
        delta = (max(self.y) - min(self.y)) * 0.15
        ax.set_xlim(min(self.y) - delta, max(self.y) + delta)
        ax.set_ylim(min(self.y) - delta, max(self.y) + delta)
        ax.set_xlabel(f'"{self.target}" fact')
        ax.set_ylabel(f'"{self.target}" calculated')
        ax.text(min(self.y), max(self.y)-delta*3, correlation_pairs, fontsize=6, fontweight ='bold')
        add_grid(ax)
        ax.legend(loc='lower right', fontsize=6)


if __name__ == '__main__':
    pass
