from parse_utils_app import get_list_of_files_in_parse_results_for_particular_team, prepare_to_parsing, \
                        get_only_filename, grab_data_for_export, export_to_excel, time_stamp
from parse_app import get_content, pars_play_content, pars_tournament_content
from proxy_config import random_proxy
import time
import random


def prepare_current_game_local_link(game_link_internal: str, team_internal: str) -> str:
    """
    Function return local link to the particular game of particular team
    :param game_link_internal: url to the particular game
    :param team_internal: parsed team as it is given in Excel file
    :returns: local link to the game from the project root
    """
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

    return f'./parse_results/{team_internal}/{game_link_internal}.html'


def perform_parse(assignment_dict, logger):
    """Main function for parsing results of basketball games according to given links
    to the teams"""
    logger.emit('clean_entirely')
    logger.emit('Parsing in progress! Please wait...')

    assignment_file = assignment_dict['assignment_file']
    assignment_tab = assignment_dict['assignment_tab']
    results_file = assignment_dict['results_file']
    results_tab = assignment_dict['results_tab']
    league = assignment_dict['league']
    season = assignment_dict['season']
    team = assignment_dict['team']

    time_to_sleep = 0.1
    # Preparation of links and local path, do some work concerning directories creation
    teams_links = prepare_to_parsing(assignment_file, assignment_tab, league, season, team, logger)
    games_links = {}
    for i, team in enumerate(teams_links):
        team_name = team[0]
        team_url = team[1]
        team_local_link = team[2]
        league = team[3]
        season = team[4]
        # sleep for a while before go to next parsing point
        time.sleep(random.random() * time_to_sleep)
        # Get content of html from link and put it in local file using proxy
        resp = get_content(team_url, team_local_link, logger, True, random_proxy)
        if resp:
            # Parse content of tournaments for particular team and store links in embedded list
            # The key of access to list in dict is short_name of the team
            logger.emit(time_stamp())
            logger.emit(f'\nThe file {team_local_link} created for team {team_name}')
            parsed_tournament_content = pars_tournament_content(team_local_link, league, season)
            main_team = parsed_tournament_content['team']
            games_links[team_name] = parsed_tournament_content['links']
            already_parsed = get_list_of_files_in_parse_results_for_particular_team(team_name)
            for game_link in games_links[team_name]:
                local_link = prepare_current_game_local_link(game_link, team[0])
                if get_only_filename(local_link, team_name) in already_parsed:
                    logger.emit(f'\nThe link {game_link} The raw file is already exists')
                    pars_play_content(local_link, main_team, logger)
                    logger.emit(f'\nThe link {game_link} was successfully parsed')
                else:
                    # sleep for a while before go to next parsing point
                    time.sleep(random.random() * time_to_sleep)
                    # print('{:~^100}'.format(game_link))
                    resp_play = get_content(game_link, local_link, True, random_proxy)
                    logger.emit(time_stamp())
                    if resp_play:
                        logger.emit(f'\nFor the file: {game_link} raw data pulled')
                        pars_play_content(local_link, main_team, logger)
                        logger.emit(f'\nThe file: {game_link} was successfully parsed')
                    else:
                        logger.emit(f"\nThe file: {game_link} wasn't parsed")

    data_to_export = grab_data_for_export()
    logger.emit(f'\nExporting to Excel status:'
                f' {export_to_excel(data_to_export, results_file, results_tab)}')
    logger.emit(f'\nParsing Finished lets start the analysis')


if __name__ == '__main__':
    pass
