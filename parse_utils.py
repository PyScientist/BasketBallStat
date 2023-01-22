from typing import List, Tuple, Union
import pandas as pd
import os
from google_auth import GoogleSheetsClient
import datetime


def time_stamp():
    print(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S'))


def get_assignment_to_parse(file_path: str, tab_internal: str) -> Union[List[Tuple[str, str, str]], None]:
    """The function get information from specified Excel file and provide it as List.
    This function also print in console the list of teams which will be parsed and updated.
    :param file_path: Full path to Excel file
    :param tab_internal: Name of tab in Excel file with information concerning teams to parse
    :returns: List of tuples with parameters for each team inside
    (short name of team, url_links, local_links)
    """
    def create_local_path(url: str) -> str:
        """creation of local path from given url"""
        folder = './parse_results/'
        path = url.replace('https://basketball.usbasket.com/', '')
        path = path.replace('/', '_')
        path = path.replace('?', '_')
        path += '.html'
        local_path = folder+path
        return local_path

    def create_description(league: str, name: str, short_name: str, link: str) -> Union[str, None]:
        """Create description of the team based on their parameters"""
        return f'{league}, {name} ({short_name}), link = {link}'

    try:
        teams_df = pd.read_excel(io=file_path, engine='openpyxl', sheet_name=tab_internal)
        teams_df['local_links'] = teams_df['Links'].map(create_local_path)
        teams_df['teams_descriptions'] = list(map(create_description, teams_df['League'],
                                                  teams_df['Teams'],
                                                  teams_df['Short names'],
                                                  teams_df['Links']))

        links_to_teams_tournament_tables = teams_df['Links'].values
        teams = teams_df['Short names'].values
        local_links = teams_df['local_links'].values
        teams_descriptions = teams_df['teams_descriptions'].values

        print('The information will be updated for the following teams:')
        for i, row in enumerate(teams_descriptions):
            print(f'{i+1}) {row}')

        return list(zip(teams, links_to_teams_tournament_tables, local_links))

    except Exception as e:
        print(f'Some exception occurred (get_assignment_to_parse): {e}')
        print('Please check the correctness of Excel file name and tab within')
        return None


def prepare_to_parsing() -> Union[List[Tuple[str, str, str]], None]:
    """Make preparation for parsing such as creation necessary folders
    :return: """

    def delete_parse_content() -> None:
        """Clear data"""
        folder = './parse_content'
        list_files = os.listdir(folder)
        for file in list_files:
            full_path = f'{folder}/{file}'
            os.remove(full_path)
            print(f'The file: {full_path} is removed')

    def create_folder_for_parse() -> None:
        """Preparation folder to store raw html"""
        folder = './parse_results'
        if os.path.isdir(folder) is False:
            try:
                os.mkdir(folder)
                print(f'{folder} created')
            except Exception as e:
                print(e)
        else:
            print(f'{folder} already exists')

    def create_folder_for_parse_content() -> None:
        """Preparation folder to store parsed content"""
        folder = './parse_content'
        if os.path.isdir(folder) is False:
            try:
                os.mkdir(folder)
                print(f'{folder} created')
            except Exception as e:
                print(e)
        else:
            print(f'{folder} already exists')

    def create_teams_parse_results_folders(teams_links_internal: List) -> None:
        """Preparation folders to store for raw html of plays results for
        teams according to excel"""
        for team in teams_links_internal:
            folder = f'./parse_results/{team[0]}'
            if os.path.isdir(folder) is False:
                try:
                    os.mkdir(folder)
                    print(f'{folder} created')
                except Exception as e:
                    print(e)
            else:
                print(f'{folder} already exists')

    excel_file_path = './jupyter/Tables_for_analysis_basketball.xlsx'
    tab = 'Teams'
    # Obtain information concerning teams need to be parsed (from Excel file).
    # Team links list has a structure (teams, links_to_teams_tournament_tables, local_links)
    teams_links_list = get_assignment_to_parse(excel_file_path, tab)
    if teams_links_list is None:
        print("The excel wasn't read")
    else:
        print("Successfully read excel continue preparations..")
        # Creation of file-structure folders
        create_folder_for_parse()
        create_folder_for_parse_content()
        create_teams_parse_results_folders(teams_links_list)
        delete_parse_content()
        print("The operations with folders finished!")
    return teams_links_list


def get_list_of_files_in_parse_results_for_particular_team(team: str) -> List:
    """look in corresponding folder for team which local html it got"""
    return os.listdir(f'./parse_results/{team}/')


def get_only_filename(full_path: str, team: str) -> str:
    """Cut file path and leave only file name"""
    return full_path.replace(f'./parse_results/{team}/', '')


def link_to_local_hash_func(game_link_internal_in: str) -> str:
    """convert url to local link"""
    game_link_internal = game_link_internal_in[:]
    game_link_internal = game_link_internal.replace('http://www.usbasket.com/', '')
    game_link_internal = game_link_internal.replace('?', '__quest_mark__')
    game_link_internal = game_link_internal.replace('https://www.usbasket.com/', '')
    return f'{game_link_internal}.html'


def grab_data_for_export() -> tuple:
    """Pull data to results of parsing csv"""

    def cleaning_dtaset(df) -> None:
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

    list_files = os.listdir(folder)

    df_tournament_list = []
    for file in list_files:
        if file != 'plays_results.csv':
            df_tournament_list.append(pd.read_csv(f'{folder}/{file}',
                                                  delimiter=";", encoding='utf-8'))

    df_tournament = pd.concat(df_tournament_list, sort=False, axis=0)

    df_merged = pd.merge(df_plays,
                         df_tournament,
                         how='inner',
                         left_on=["main_team", "local_name"],
                         right_on=["Team", "Local_name"])

    cleaning_dtaset(df_merged)

    return tuple([df_plays, df_tournament, df_merged])


def export_to_excel(data_in: tuple) -> bool:
    try:
        with pd.ExcelWriter('jupyter/results.xlsx', engine='xlsxwriter') as writer:
            data_in[0].to_excel(writer, sheet_name='plays', index=False)
            data_in[1].to_excel(writer, sheet_name='tournament', index=False)
            data_in[2].to_excel(writer, sheet_name='combine', index=False)
            print('results have writen to Excel')
        return True
    except Exception as e:
        print(f'While exporting to Excel an error occurred {e}')
        return False


def export_to_google_sheets(data_in: tuple) -> bool:
    try:
        gs_client = GoogleSheetsClient()
        gs_client.set_data_to_particular_sheet('Tables_for_analysis_basketball', 'plays', data_in[0])
        return True
    except Exception as e:
        print(f'While exporting to Google sheets an error occurred {e}')
        return False


if __name__ == '__main__':
    data = grab_data_for_export()
    export_to_excel(data)

