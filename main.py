from parse_utils import prepare_to_parsing, \
                        get_list_of_files_in_parse_results_for_particular_team,\
                        get_only_filename,\
                        grab_data_for_export, export_to_excel, export_to_google_sheets
from parse_utils import time_stamp
from parse import get_content, pars_play_content, pars_tournament_content
from proxy_config import random_proxy
from typing import Tuple
import time
import random


def perform_parse():
    """Main function for parsing results of basketball games"""
    def prepare_current_game_local_link(game_link_internal: str, team_internal: Tuple[str, str, str]) -> str:
        game_link_internal = game_link_internal.replace('http://www.usbasket.com/', '')
        game_link_internal = game_link_internal.replace('?', '__quest_mark__')
        game_link_internal = game_link_internal.replace('https://www.usbasket.com/', '')
        return f'./parse_results/{team_internal[0]}/{game_link_internal}.html'

    time_to_sleap = 0.2

    time_stamp()
    print('Preparing for parsing...')
    teams_links = prepare_to_parsing()
    time_stamp()
    print('Parsing is launching...')
    games_links = {}
    for i, team in enumerate(teams_links):
        team_name = team[0]
        team_url = team[1]
        team_local_link = team[2]
        # sleep for a while before go to next parsing point
        time.sleep(random.random() * time_to_sleap)
        # Get content of html from link and put it in local file using proxy
        resp = get_content(team_url, team_local_link, True, random_proxy)
        if resp:
            # Parse content of tournaments for particular team and store links in embedded list
            # The key of access to list in dict is short_name of the team
            time_stamp()
            print(f'The file {team_local_link} created for team {team_name}')
            parsed_tournament_content = pars_tournament_content(team_local_link)
            main_team = parsed_tournament_content['team']
            games_links[team_name] = parsed_tournament_content['links']
            already_parsed = get_list_of_files_in_parse_results_for_particular_team(team_name)
            for game_link in games_links[team_name]:
                local_link = prepare_current_game_local_link(game_link, team)
                if get_only_filename(local_link, team_name) in already_parsed:
                    print(f'The link {game_link} The raw file is already exists')
                    pars_play_content(local_link, main_team)
                    print(f"The link {game_link} was successfully parsed")
                else:
                    # sleep for a while before go to next parsing point
                    time.sleep(random.random() * time_to_sleap)
                    # print('{:~^100}'.format(game_link))
                    resp_play = get_content(game_link, local_link, True, random_proxy)
                    time_stamp()
                    if resp_play:
                        print(f"For the file: {game_link} raw data pulled")
                        pars_play_content(local_link, main_team)
                        print(f"The file: {game_link} was successfully parsed")
                    else:
                        print(f"The file: {game_link} wasn't parsed")

    data_to_export = grab_data_for_export()
    print(f'Exporting to Excel status: {export_to_excel(data_to_export)}')
    print(f'Exporting to GoogleSheets status: {export_to_google_sheets(data_to_export)}')


if __name__ == '__main__':
    perform_parse()
