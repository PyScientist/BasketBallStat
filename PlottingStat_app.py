from matplotlib import pyplot as plt


def show_basic_comp_hist(df, features, target, df_pred_data, opponent, homeflag, date, days=200) -> None:

    curve_colors_dict = {
        'PTS #1': 'red',
        'PTS #2': '#B3B3B3',
        'Total points': 'orange',
    }

    columns = features.copy()
    columns.extend([target])

    df_last = df[(df['TimeShift'] >= -days) & (df['TimeShift'] < 0)]  # За последние X дней.
    df_last_same_team = df_last[df_last['Team #2'] == opponent]  # За последние X дней с той же командой.
    df_last_same_field = df_last[df_last['Home flag'] == homeflag]  # За последние X дней на том же стадионе.

    fig, ax = plt.subplots(len(columns), len(columns), figsize=(len(columns)*5, len(columns)*5))
    plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.25, hspace=0.25)

    for x, column_x in enumerate(columns):
        for y, column_y in enumerate(columns):
            if column_y == target:
                color_main = curve_colors_dict[target]
            else:
                color_main = 'blue'

            color_model_used = 'green'
            color_last = '#C9DB74'
            color_same_team = '#DCB0F2'
            color_same_field = '#8BE0A4'

            if column_x == column_y:
                ax[x, y].hist(df[column_x],
                              bins=20,
                              color=color_main,
                              label='Все данные')
                ax[x, y].hist(df_last[column_x],
                              bins=20,
                              color=color_last,
                              label=f'Последние {days} дней')
                ax[x, y].hist(df_last_same_field[column_x],
                              bins=20,
                              color=color_same_field,
                              label=f'Та же площадка последние {days} дней')
                ax[x, y].set_xlabel(column_y)
                ax[x, y].set_ylabel('Частость')
                ax[x, y].legend(loc='upper right', fontsize=6)
            else:
                ax[x, y].scatter(df[column_x], df[column_y], c=color_main, label='Все данные')
                ax[x, y].scatter(df_last_same_team[column_x],
                                 df_last_same_team[column_y],
                                 c=color_same_team,
                                 s=150,
                                 marker="s",
                                 label=f'С той же командой (последние{days} дней)')
                ax[x, y].scatter(df_last_same_field[column_x],
                                 df_last_same_field[column_y],
                                 c=color_same_field,
                                 s=130,
                                 marker="p",
                                 label=f'Та же площадка (последние {days} дней)')
                ax[x, y].scatter(df_last[column_x],
                                 df_last[column_y],
                                 c=color_last,
                                 label=f'Последние {days} дней')
                ax[x, y].scatter(df_pred_data[column_x],
                                 df_pred_data[column_y],
                                 c=color_model_used,
                                 s=170,
                                 marker="*",
                                 label='Медианные исп. в модели по группам')
                ax[x, y].set_xlabel(column_x)
                ax[x, y].set_ylabel(column_y)
                ax[x, y].legend(loc='lower right', fontsize=6)

    team = df['main_team'].unique()

    fig.savefig(f'./model_substantiation_{target}{date}_{team[0]}_vs_{opponent}.png')