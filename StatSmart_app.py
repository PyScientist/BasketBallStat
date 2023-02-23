import datetime
import pandas as pd
import numpy as np


class TeamStatSmart:
    """
    Для того чтобы подать на вход прогноза значения параметров
    """

    def __init__(self, single_team_analysis, op_team, home_flag, direction='opposite', time_frames=(0, 200)):
        self.type = None
        self.team = single_team_analysis['t_name']  # название анализируемой команды
        self.df_init = single_team_analysis['df']  # Дата фрейм по команде

        # выбираем статистику в определенных временных рамках если статистики недостаточно выбираем минимум 100 матчей
        start_counter = time_frames[0]
        end_counter = -time_frames[1]
        shape = 0
        iterations = 0
        while ((shape < 10) and (iterations < 10)):
            self.df = self.df_init.copy()
            self.df = self.df[(self.df_init['TimeShift'] >= end_counter) & (self.df_init['TimeShift'] < start_counter)]
            shape = self.df.shape[0]
            end_counter -= 5
            iterations += 1

        self.op_team = op_team  # Название команды - соперника анализируемой команды

        params = ['2PA #1', '2P% #1', '3PA #1', '3P% #1', 'FTA #1', 'FT% #1',
                  'ORB #1', 'DRB #1', 'TRB #1', 'AST #1', 'F #1',
                  'STL #1', 'BLK #1', 'TOV #1', 'PTS #1', 'Total points']

        params_subs = ['2PA #2', '2P% #2', '3PA #2', '3P% #2', 'FTA #2', 'FT% #2',
                       'ORB #2', 'DRB #2', 'TRB #2', 'AST #2', 'F #2',
                       'STL #2', 'BLK #2', 'TOV #2', 'PTS #2', 'Total points']

        '''Указываем для какой команды собираем статистику, для анализируемой (direct) или соперника (opposite)
        в зависимости от этого изменяем метод поиска флага домашней игры и номер параметров #1, #2.'''
        params_subs_dict = {}
        if direction == 'direct':
            self.home_flag = home_flag
            for i in range(len(params)):
                params_subs_dict[params[i]] = params[i]
        elif direction == 'opposite':
            self.home_flag = {0: 1, 1: 0}[home_flag]
            for i in range(len(params)):
                params_subs_dict[params[i]] = params_subs[i]

        stat_param = ['min', "mean", np.median, 'max', "count"]

        # Ищем такие же игры команды (дома или на выезде) и с тем же соперником
        self.df_1ds = self.df[(self.df['Team #2'] == self.op_team) & (self.df['Home flag'] == self.home_flag)]
        # display('Ищем такие же игры команды (дома или на выезде) и с тем же соперником', self.df_1ds)
        self.stat1 = self.df_1ds[params].reset_index(drop=True).agg(stat_param)
        self.stat1.rename(columns=params_subs_dict, inplace=True)
        # Ищем такие же игры команды с тем же соперником
        self.df_2ds = self.df[(self.df['Team #2'] == self.op_team)]
        # display('Ищем такие же игры команды с тем же соперником', self.df_2ds)
        self.stat2 = self.df_2ds[params].reset_index(drop=True).agg(stat_param)
        self.stat2.rename(columns=params_subs_dict, inplace=True)
        # Ищем такие же игры команды (дома или на выезде)
        self.df_3ds = self.df[(self.df['Home flag'] == self.home_flag)]
        # display('Ищем такие же игры команды (дома или на выезде)', self.df_3ds)
        self.stat3 = self.df_3ds[params].reset_index(drop=True).agg(stat_param)
        self.stat3.rename(columns=params_subs_dict, inplace=True)
        # Ищем все игры с командой
        self.stat4 = self.df[params].reset_index(drop=True).agg(stat_param)
        self.stat4.rename(columns=params_subs_dict, inplace=True)

    def get_param(self, name, type_stat):
        """
        Функция для выбора какой вариант параметра будем возвращать
        в зависимости от объёма статистики по предыдущим матчам.
        :param name: имя параметра (фактически - это колонка дата фрейма статистики)
        :param type_stat: тип описательной статистики (фактически индекс дата фрейма статистики)
        """
        if self.stat1.loc['count', type_stat] > 3:
            self.type = 'By the games with the same field and same opponent'
            return self.stat1.loc[name, type_stat]
        elif (self.stat1.loc['count', type_stat] > 1) & (self.stat3.loc['count', type_stat] > 10):
            self.type = 'By the games with the same field and same opponent and on the same field avg.'
            return (self.stat1.loc[name, type_stat] + self.stat3.loc[name, type_stat])/2

        elif self.stat2.loc['count', type_stat] > 3:
            self.type = 'By the games with the same opponent'
            return self.stat2.loc[name, type_stat]
        elif (self.stat2.loc['count', type_stat] > 2) & (self.stat3.loc['count', type_stat] > 10):
            self.type = 'By the games with the same opponent and on the same field avg.'
            return (self.stat2.loc[name, type_stat] + self.stat3.loc[name, type_stat])/2
        
        elif self.stat3.loc['count', type_stat] > 10:
            self.type = 'By the games on the same field'
            return self.stat3.loc[name, type_stat]
        else:
            self.type = 'By all games'
            return self.stat4.loc[name, type_stat]


class DataForPrediction:
    def __init__(self, df_main, team, op_team, home_flag, next_play_date=datetime.date.today(), time_frames=(0, 200)):
        """
        :param team: Для какой команды прогнозируем счет.
        :param df_main: main dataframe imported from combined tab (Results).
        :param home_flag: На чьем поле будет игра (1 - домашнее поле, 0 - на выезде).
        :param op_team: C какой командой будет играть анализируемая команда.
        :param next_play_date: Дата игры для которой осуществляется прогноз (по умолчанию текущая дата).
        :param time_frames: Временной промежуток в рамках которого анализируются игры для поиска медианы.
        """
        self.df_main = df_main
        self.team = team
        self.op_team = op_team
        self.home_flag = home_flag
        self.next_play_date = next_play_date
        self.time_frames = time_frames
        self.data_for_prediction = None
        self.prepare_prediction_data()

    def prepare_prediction_data(self):
        # Перечислим параметры для которых будут собираться значения для анализируемой команды
        params = ['2PA #1', '2P% #1', '3PA #1', '3P% #1', 'FTA #1', 'FT% #1',
                  'ORB #1', 'DRB #1', 'TRB #1', 'AST #1', 'F #1',
                  'STL #1', 'BLK #1', 'TOV #1', 'PTS #1', 'Total points']

        # Перечислим параметры для которых будут собираться значения для команды соперника
        params_subs = ['2PA #2', '2P% #2', '3PA #2', '3P% #2', 'FTA #2', 'FT% #2',
                       'ORB #2', 'DRB #2', 'TRB #2', 'AST #2', 'F #2',
                       'STL #2', 'BLK #2', 'TOV #2', 'PTS #2']

        # Укажем какой именно статистический параметр будем возвращать
        stat_param = 'median'

        # Возьмем медианные результаты команды для которой осуществляется прогноз
        an_team_stat = TeamStatSmart(perform_single_team_analysis(self.team,
                                                                  self.df_main,
                                                                  self.next_play_date,
                                                                  time_frames=self.time_frames),
                                     self.op_team,
                                     self.home_flag,
                                     direction='direct',
                                     time_frames=self.time_frames)
        median_an = [an_team_stat.get_param(stat_param, param) for param in params]

        # Возьмем медианные результаты команды оппонента анализируемой команды
        op_team_stat = TeamStatSmart(perform_single_team_analysis(self.op_team,
                                                                  self.df_main,
                                                                  self.next_play_date,
                                                                  time_frames=self.time_frames),
                                     self.team,
                                     self.home_flag,
                                     direction='opposite',
                                     time_frames=self.time_frames)
        median_op = [op_team_stat.get_param(stat_param, param) for param in params_subs]

        # Компонуем общий дата сет для прогноза
        df_dict, headers, values = {}, [], []
        headers.extend(params)
        headers.extend(params_subs)
        headers.append('Home flag')
        values.extend(median_an)
        values.extend(median_op)
        values.append(self.home_flag)

        for i in range(len(headers)):
            df_dict[headers[i]] = values[i]

        self.data_for_prediction = pd.DataFrame(df_dict, index=[stat_param])


def convert_date(str_date: str) -> datetime.date:
    month_dict = {
        'January': 1,
        'February': 2,
        'March': 3,
        'April': 4,
        'May': 5,
        'June': 6,
        'July': 7,
        'August': 8,
        'September': 9,
        'October': 10,
        'November': 11,
        'December': 12,
        }
    month, day, year = str_date.split(' ')
    return datetime.date.fromisoformat('{}-{:0>2}-{:0>2}'.format(year, month_dict[month], day.replace(',', '')))


def calc_time_shift(date_in, next_play_date_in):
    """return: amount of days shift -backward, +forward"""
    return (convert_date(date_in) - next_play_date_in).total_seconds() / (3600 * 24)


def perform_single_team_analysis(team: str, df_main, next_play_date=datetime.date.today(), time_frames=(0, 200)):
    """Function for single team analysis"""

    def printing_func(string, printing='no'):
        """function to enable or disable printing information of analysis"""
        if printing == 'yes':
            print(string)

    def replace_to_nan(val):
        """Function to remove self correlation indexes"""
        if val == 1:
            val = np.nan
        return val

    printing_func(f'Currently analyse the following team {team}')
    # Получаем все записи из основной таблицы по этой команде.

    start_counter = time_frames[0]
    end_counter = -time_frames[1]
    shape = 0
    iterations = 0
    while ((shape < 10) and (iterations < 10)):
        df_team_to_analyse = df_main[df_main['Team #1'] == team].copy()

        df_team_to_analyse['TimeShift'] = [calc_time_shift(date, next_play_date) for date in df_team_to_analyse['Date']]

        # Cut set cording to given timeframes
        df_team_to_analyse = df_team_to_analyse[(df_team_to_analyse['TimeShift'] >= end_counter) &
                                                (df_team_to_analyse['TimeShift'] < start_counter)]
        shape = df_team_to_analyse.shape[0]
        end_counter -= 20
        iterations+=1

    # Убеждаемся, что видим все записи
    printing_func(df_team_to_analyse.columns.values)
    # Дополнительно смотрим сколько игр сыграно командами.
    printing_func('For {} there were ({}) games played'.format(team, df_team_to_analyse.shape[0]))
    # Настраиваем с учетом каких значимых фитч и целевых показателей будет выполняться анализ.
    important_features = ['2PA #1', '2P% #1', '3PA #1', '3P% #1',
                          'FTA #1', 'FT% #1', 'ORB #1', 'DRB #1',
                          'TRB #1', 'AST #1', 'F #1', 'STL #1', 'BLK #1', 'TOV #1', 'PTS #1', 'Home flag']

    important_features_of_second_team = ['2PA #2', '2P% #2', '3PA #2', '3P% #2',
                                         'FTA #2', 'FT% #2', 'ORB #2', 'DRB #2', 'TRB #2',
                                         'AST #2', 'F #2', 'STL #2', 'BLK #2', 'TOV #2', 'PTS #2']

    chosen_targets = ['Total points', 'PTS #1', 'Victory flag', 'PTS #2',
                      '2PA #1', '2P% #1', '3PA #1', '3P% #1',
                      'FTA #1', 'FT% #1', 'ORB #1', 'DRB #1',
                      'TRB #1', 'AST #1', 'F #1', 'STL #1', 'BLK #1', 'TOV #1',
                      '2PA #2', '2P% #2', '3PA #2', '3P% #2',
                      'FTA #2', 'FT% #2', 'ORB #2', 'DRB #2', 'TRB #2',
                      'AST #2', 'F #2', 'STL #2', 'BLK #2', 'TOV #2']

    chosen_params = []
    chosen_params.extend(important_features)
    chosen_params.extend(chosen_targets)
    chosen_params = list(set(chosen_params))
    extended_params = []
    extended_params.extend(chosen_params)
    extended_params.extend(important_features_of_second_team)
    extended_params = list(set(extended_params))
    exclude_list = [x for x in list(df_team_to_analyse.columns.values) if x not in extended_params]
    printing_func('{:~^120}'.format(''))
    printing_func('Important_features - {}, {}'.format(important_features, len(important_features)))
    printing_func('{:~^120}'.format(''))
    printing_func('Important_features_of_second_team - {}, {}'.format(important_features_of_second_team,
                                                                      len(important_features_of_second_team)))
    printing_func('{:~^120}'.format(''))
    printing_func('Choose targets - {}, {}'.format(chosen_targets, len(chosen_targets)))
    printing_func('{:~^120}'.format(''))
    printing_func('Choose params - {}, {}'.format(chosen_params, len(chosen_params)))
    printing_func('{:~^120}'.format(''))
    printing_func('Extended_params - {}, {}'.format(extended_params, len(extended_params)))
    printing_func('{:~^120}'.format(''))
    printing_func('Exclude_list - {}, {}'.format(exclude_list, len(exclude_list)))

    # Для того, что-бы построить корреляционную матрицу, нам нужно
    # взять только числовые значения (остальные не имеют смысла).
    corr_matrix = df_team_to_analyse.drop(columns=exclude_list, axis=1, inplace=False).corr()

    # По диагонали будут парные корреляции равные единице. Убираем эти значения в nan
    for column in corr_matrix.columns:
        corr_matrix[column] = list(map(lambda x: replace_to_nan(x), corr_matrix[column]))

    pd.set_option("display.max_columns", None)
    pd.set_option("display.max_rows", None)

    target_corr_matrix = corr_matrix[chosen_targets]

    return {
        'df': df_team_to_analyse,  # Дата фрейм для определенной команды
        'params': extended_params,  # Список параметров которые принимаются во внимание при анализе
        'params_second': important_features_of_second_team,  # Список параметров для второй команды
        't_name': team,  # Название команды
        'c_matrix': target_corr_matrix,  # Корреляционная матрица команды
        'targets': chosen_targets,  # целевых параметров, которые принимаются во внимание
    }


if __name__ == '__main__':
    pass
