from typing import List, Tuple, Union
import pandas as pd
import os
import datetime

from PySide2 import QtCore


def time_stamp() -> datetime.datetime:
    return f"\n{datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')}"


def get_assignment_to_parse(assignment_path: str,
                            tab_internal: str,
                            league_in: list,
                            season_in: list,
                            team_in: list,
                            logger: QtCore.Signal) -> Union[List[Tuple[str, str, str, str, str]], None]:
    """
    The function get information from specified Excel file and provide it as List.
    This function also print in console the list of teams which will be parsed and updated.
    :param assignment_path: Full path to Excel file with assignment for parsing
    :param tab_internal: Name of tab in Excel file with information concerning teams to parse
    :param league_in: League to perform parsing
    :param season_in: Season to perform parsing
    :param team_in: Team to perform parsing
    :param logger: logger to transit signals
    :returns: List of tuples with parameters for each team inside
    (short name of team, url_links, local_links, leagues, seasons)
    """
    def create_local_path(url: str) -> str:
        """
        Creation of local path from given url!
        the url (tournament table page for particular team)
        is taken from Excel file and is given to the function
        :parameter url: url from list was obtained fom Excel file
        :returns: full local path from the root of the project
        """
        replaces_first = {
            'https://basketball.usbasket.com/': '',
            'http://www.eurobasket.com/': '',
            'https://www.eurobasket.com/': '',
            'http://basketball.eurobasket.com/': '',
            'https://basketball.eurobasket.com/': '',
            'https://basketball.asia-basket.com/': '',
            'https://basketball.latinbasket.com/': '',
            }

        replaces_second = {
            '/': '_',
            '?': '_',
            }

        folder = './parse_results/'
        path = url
        for key in replaces_first:
            path = path.replace(key, replaces_first[key])
        for key in replaces_second:
            path = path.replace(key, replaces_second[key])

        return f'{folder}{path}.html'

    def create_description(league: str, name: str, short_name: str, link: str) -> Union[str, None]:
        """Create description of the team based on their parameters"""
        return f'{league}, {name} ({short_name}), link = {link}'

    try:
        assignment_df = pd.read_excel(io=assignment_path, engine='openpyxl', sheet_name=tab_internal)

        teams_df = assignment_df[assignment_df['League'] == league_in].copy()

        if season_in != 'All':
            teams_df = teams_df[teams_df['Season'] == season_in].copy()
        if team_in != 'All':
            teams_df = teams_df[teams_df['Teams'] == team_in].copy()

        teams_df['local_links'] = teams_df['Links'].map(create_local_path)
        teams_df['teams_descriptions'] = list(map(create_description, teams_df['League'],
                                                  teams_df['Teams'],
                                                  teams_df['Short names'],
                                                  teams_df['Links']))

        links_to_teams_tournament_tables = teams_df['Links'].values
        teams = teams_df['Short names'].values
        local_links = teams_df['local_links'].values
        leagues = teams_df['League']
        seasons = teams_df['Season']

        teams_descriptions = teams_df['teams_descriptions'].values

        log = 'The information will be updated for the following links:\n'
        for i, row in enumerate(teams_descriptions):
            log += f'\n{i + 1}) {row}'

        logger.emit(f'\n{log}')

        return list(zip(teams, links_to_teams_tournament_tables, local_links, leagues, seasons))

    except Exception as e:
        print(f'Some exception occurred (get_assignment_to_parse): {e}')
        print('Please check the correctness of Excel file name and tab within')
        return None


def prepare_to_parsing(assignment_file: str,
                       assignment_tab: str,
                       league_in: list,
                       season_in: list,
                       team_in: list,
                       logger: QtCore.Signal) -> Union[List[Tuple[str, str, str, str, str]], None]:
    """
    Make preparation for parsing such as creation necessary folders
    :return:
    :param assignment_file: Full path to Excel file with assignment for parsing
    :param assignment_tab: Name of tab in Excel file with information concerning teams to parse
    :param league_in: League to perform parsing
    :param season_in: Season to perform parsing
    :param team_in: Team to perform parsing
    :param logger: logger to transit signals by emit method call
    """

    def create_folder_for_parse(logger_in: QtCore.pyqtBoundSignal) -> None:
        """Preparation folder to store raw html"""
        folder = './parse_results'
        if os.path.isdir(folder) is False:
            try:
                os.mkdir(folder)
                logger_in.emit(f'\n{folder} created')
            except Exception as e:
                logger_in.emit(f'\n{e}')
        else:
            logger_in.emit(f'\n{folder} already exists')

    def create_folder_for_parse_content(logger_in: QtCore.pyqtBoundSignal) -> None:
        """Preparation folder to store parsed content"""
        folder = './parse_content'
        if os.path.isdir(folder) is False:
            try:
                os.mkdir(folder)
                logger_in.emit(f'\n{folder} created')
            except Exception as e:
                logger_in.emit(f'\n{e}')
        else:
            logger_in.emit(f'\n{folder} already exists')

    def create_teams_parse_results_folders(teams_links_internal: List, logger_in: QtCore.pyqtBoundSignal) -> None:
        """Preparation folders to store for raw html of plays results for
        teams according to excel"""
        for team in teams_links_internal:
            folder = f'./parse_results/{team[0]}'
            if os.path.isdir(folder) is False:
                try:
                    os.mkdir(folder)
                    logger_in.emit(f'\n{folder} created')
                except Exception as e:
                    logger_in.emit(f'\n{e}')
            else:
                logger_in.emit(f'\n{folder} already exists')

    def delete_parse_content(logger_in: QtCore.pyqtBoundSignal) -> None:
        """Clear data"""
        folder = './parse_content'
        list_files = os.listdir(folder)
        for file in list_files:
            full_path = f'{folder}/{file}'
            os.remove(full_path)
            logger_in.emit(f'\nThe file: {full_path} is removed')

    # Obtain information concerning teams need to be parsed (from Excel file).
    # Team links list has a structure (teams, links_to_teams_tournament_tables, local_links)
    teams_links_list = get_assignment_to_parse(assignment_file, assignment_tab,
                                               league_in, season_in, team_in, logger)
    if teams_links_list is None:
        logger.emit(f"\nThe excel wasn't read")
    else:
        logger.emit(f'\nSuccessfully read excel continue preparations...')
        # Creation of file-structure folders
        create_folder_for_parse(logger)
        create_folder_for_parse_content(logger)
        create_teams_parse_results_folders(teams_links_list, logger)
        delete_parse_content(logger)
        logger.emit(f'\nThe operations with folders finished!')

    return teams_links_list


def get_list_of_files_in_parse_results_for_particular_team(team: str) -> List:
    """look in corresponding folder for team which local html it got"""
    return os.listdir(f'parse_results/{team}/')


def get_only_filename(full_path: str, team: str) -> str:
    """Cut file path and leave only file name"""
    return full_path.replace(f'./parse_results/{team}/', '')


def link_to_local_hash_func(game_link_internal_in: str) -> str:
    """
    Convert url (for results of the game) to local link
    used to check is the given url already parsed or not.
    :parameter game_link_internal_in: url link to the game.
    :returns: local path to the game from the root.
    """
    game_link_internal = game_link_internal_in[:]

    replaces_first = {
        'http://www.usbasket.com/': '',
        'https://www.usbasket.com/': '',
        'http://www.eurobasket.com/': '',
        'https://www.eurobasket.com/': '',
        'http://www.asia-basket.com/': '',
        'https://www.asia-basket.com/': '',
        'http://www.latinbasket.com/': '',
        'https://www.latinbasket.com/': '',
        '?': '__quest_mark__',
        }

    for key in replaces_first:
        game_link_internal = game_link_internal.replace(key, replaces_first[key])

    return f'{game_link_internal}.html'


def grab_data_for_export() -> tuple:
    """Pull data to results of parsing csv"""

    def cleaning_dataset(df) -> None:
        """Clean dataframe for following manipulation"""
        delete_columns_list = [
            'local_name', 'PM2_1',
            'PM3_1', 'FTM_1', 'RV_1', 'AG_1',
            'PM2_2', 'PM3_2', 'FTM_2', 'RV_2', 'AG_2', 'Team',
            'Game', 'Date', 'League',
        ]
        rename_columns_dict = {
            'league': 'League',
            'game': 'Round',
            'date': 'Date',
            'team1': 'Team #1',
            'A2_1': '2PA #1',
            'A2PERC_1': '2P% #1',
            'A3_1': '3PA #1',
            'A3PERC_1': '3P% #1',
            'FA_1': 'FTA #1',
            'FAPERC_1': 'FT% #1',
            'OFF_1': 'ORB #1',
            'DEF_1': 'DRB #1',
            'RB_1': 'TRB #1',
            'AS_1': 'AST #1',
            'F_1': 'F #1',
            'ST_1': 'STL #1',
            'FV_1': 'BLK #1',
            'TO_1': 'TOV #1',
            'PT_1': 'PTS #1',
            'RNK_1': 'RNK #1',
            'team2': 'Team #2',
            'A2_2': '2PA #2',
            'A2PERC_2': '2P% #2',
            'A3_2': '3PA #2',
            'A3PERC_2': '3P% #2',
            'FA_2': 'FTA #2',
            'FAPERC_2': 'FT% #2',
            'OFF_2': 'ORB #2',
            'DEF_2': 'DRB #2',
            'RB_2': 'TRB #2',
            'AS_2': 'AST #2',
            'F_2': 'F #2',
            'ST_2': 'STL #2',
            'FV_2': 'BLK #2',
            'TO_2': 'TOV #2',
            'PT_2': 'PTS #2',
            'RNK_2': 'RNK #2',
            'Team_at_home': 'Team at home',
            'Team_outside': 'Team away',
            'Home_flag': 'Home flag',
            'Score_home_team': 'Home team score',
            'Score_outside_team': 'Outside team score',
            'Sum_score': 'Total points',
            'Victory_flag': 'Victory flag',
            'Local_name': 'Local path',
            'Link': 'Url',
        }
        df.drop(columns=delete_columns_list, axis=1, inplace=True)
        df.rename(columns=rename_columns_dict, inplace=True)

    folder = './parse_content'
    file_plays = 'plays_results.csv'

    df_plays = pd.read_csv(f'{folder}/{file_plays}', delimiter=";", encoding='utf-8')
    df_plays.drop_duplicates(inplace=True)

    def unify_team_names(name: str, column_type: str) -> str:
        """
        Replace the name of the team to fet it particular standards.
        :param name: the current name of the team;
        :param column_type: type of column (capital or lowercase for correct changing);
        :return: converted string representation of team name for particular case.
        """

        if column_type == 'uppercase':
            replace_dict = {
                'GOLDEN ST.W.': 'GS WARRIORS',
                'INDIANA P': 'INDIANA P.',
                'NEW YORK K.': 'NY KNICKS',
                'PHOENIX SUNS': 'PHOENIX S.',
                }
        elif column_type == 'lowercase':
            replace_dict = {
                'Golden St.W.': 'GS Warriors',
                'Indiana P': 'Indiana P.',
                'New York K.': 'NY Knicks',
                'Phoenix Suns': 'Phoenix S.',
                }
        else:
            replace_dict = {}

        if name in replace_dict:
            return replace_dict[name]
        else:
            return name

    df_plays['main_team'] = list(map(lambda x: unify_team_names(x, 'lowercase'), df_plays['main_team']))
    df_plays['team1'] = list(map(lambda x: unify_team_names(x, 'uppercase'), df_plays['team1']))
    df_plays['team2'] = list(map(lambda x: unify_team_names(x, 'uppercase'), df_plays['team2']))

    list_files = os.listdir(folder)

    df_tournament_list = []
    for file in list_files:
        if file != 'plays_results.csv':
            df_tournament_list.append(pd.read_csv(f'{folder}/{file}',
                                                  delimiter=";", encoding='utf-8'))

    df_tournament = pd.concat(df_tournament_list, sort=False, axis=0)
    df_tournament.drop_duplicates(inplace=True)

    df_tournament['Team'] = list(map(lambda x: unify_team_names(x, 'lowercase'), df_tournament['Team']))
    df_tournament['Team_at_home'] = list(map(lambda x: unify_team_names(x, 'uppercase'), df_tournament['Team_at_home']))
    df_tournament['Team_outside'] = list(map(lambda x: unify_team_names(x, 'uppercase'), df_tournament['Team_outside']))

    df_merged = pd.merge(df_plays,
                         df_tournament,
                         how='inner',
                         left_on=["main_team", "local_name"],
                         right_on=["Team", "Local_name"])

    cleaning_dataset(df_merged)

    return tuple([df_plays, df_tournament, df_merged])


def export_to_excel(data_in: tuple,
                    excel_file_path: str,
                    tab_name: str,) -> str:

    if os.path.isfile(excel_file_path):
        previous_data_df = pd.read_excel(io=excel_file_path,
                                         engine='openpyxl',
                                         sheet_name='Results')
        # Compare two dataframes and prepare combined stacked one over another
        combined_df = pd.concat([previous_data_df, data_in[2]]).reset_index(drop=True)
        combined_df.drop_duplicates(inplace=True)
    else:
        combined_df = data_in[2]

    try:
        with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
            combined_df.to_excel(writer, sheet_name=tab_name, index=False)
        return f'Results have writen to Excel {excel_file_path}'
    except Exception as e:
        return f'While exporting to Excel an error occurred {e}'


if __name__ == '__main__':
    pass
