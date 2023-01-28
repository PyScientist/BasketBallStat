import requests
from requests import Session
from bs4 import BeautifulSoup
import bs4
import fake_useragent
from typing import Tuple, Dict
import os
from parse_utils import link_to_local_hash_func


def get_content(url: str, file_path: str, proxies_flag=False, random_proxy=None) -> bool:
    """Got content from url and put it into local file
    It can be also proxy can be used"""
    def write_response_to_file(response_in: requests.models.Response, file_path_in: str) -> None:
        with open(file_path_in, 'w', encoding='utf-8') as f:
            f.write(response_in.text)

    user_agent = fake_useragent.UserAgent().random
    header = {'user-agent': user_agent}
    session = Session()
    session.headers.update(header)

    try:
        if proxies_flag and random_proxy is not None:
            response, proxy = random_proxy(url)
            print(f'to get response used: {proxy}')
        else:
            response = session.get(url, headers=header)
        if response is None:
            print(f'{url} is not connected to proxy')
            return False
        else:
            write_response_to_file(response, file_path)
        return True
    except Exception as e:
        print(f'Some exception {e} occurred')
        return False


def pars_tournament_content(url: str, league: str, season: str) -> Dict:
    """Write results of parsing for tournament table in csv file
    :param url: link to tournament page
    :param league: Tournament league (for example NBA)
    :param season: years of tournament (for example 2021-2022)
    """
    dict_play_result = {
        'https://www.eurobasket.com/images/minus.png': 0,
        'https://www.eurobasket.com/images/plus.png': 1,
    }

    GET_SINGLE_PLAY_RETURN = [Tuple, None]

    def write_parce_results_in_file(data: Dict, season: str) -> Dict:
        path = f'./parse_content/{data["team"]}_tournament_schedule_{season}.csv'
        with open(path, 'w', encoding='utf-8') as f:
            header = "Team;Game;" \
                     "Date;League;" \
                     "Team_at_home;Team_outside;Home_flag;" \
                     "Score_home_team;Score_outside_team;Sum_score;" \
                     "Victory_flag;Local_name;Link;season\n"
            f.write(header)
            for row in data['plays']:
                items = ''
                for i, item in enumerate(row):
                    if i+1 < len(row):
                        items+=f'{str(item)};'
                    else:
                        items += f'{str(item)};{season}\n'
                f.write(items)

    def get_single_play(td_records: bs4.element.ResultSet, team: str, season: str, league: str) -> GET_SINGLE_PLAY_RETURN:

        if  (season == '2021-2022') or (season == '2020-2021'):
            print('------------------------', len(td_records))
            print(td_records)
            print('------------------------')
            score_sell = td_records[3]
            round_sell = td_records[1]
            team_cell = td_records[2]
        elif season == '2022-2023':
            score_sell = td_records[4]
            round_sell = td_records[2]
            team_cell = td_records[3]

        if score_sell.find('a') is not None:
            if score_sell.find('a').contents[0] == 'History':
                pass
            else:
                date = td_records[0].contents[0]
                if (season == '2021-2022') or (season == '2020-2021'):
                    league = league
                    game = round_sell.contents[0]
                elif season == '2022-2023':
                    league = td_records[1].find('img')['title']
                    game = round_sell.find('span', class_='rnd_desktop').contents[0]

                team_at_home = team_cell.find('span', class_='spnt2').contents[0].contents[0]
                team_outside = team_cell.find('span', class_='spnt1').contents[0].contents[0]
                link = score_sell.find('a')['href'].strip()
                score_outside_team, score_home_team = score_sell.find('a').contents[0].split('-')
                victory_flag = dict_play_result[score_sell.find('img')['src']]

                sum_score = int(score_home_team) + int(score_outside_team)

                if team_at_home == team:
                    home_flag = 1
                else:
                    home_flag = 0

                return (team, game, date,
                        league, team_at_home,
                        team_outside, home_flag, score_home_team,
                        score_outside_team, sum_score, victory_flag, link_to_local_hash_func(link), link)
            return None
        else:
            return None

    with open(url, 'r', encoding='utf-8') as f:
        response = f.read()
    soup = BeautifulSoup(response, 'lxml')

    if (season == '2021-2022') or (season == '2020-2021'):
        game_schedule_records = soup.find_all('tr', class_='Mnewstext')[1:]
    elif season == '2022-2023':
        game_schedule_records = soup.find_all('tr', class_='Mnewstext new_games_list')

    team = soup.find("td", class_="authorstitle gameschedule_full_tbl_team").contents
    if (season == '2021-2022') or (season == '2020-2021'):
        team = team[0].replace('\xa0', '').replace(' Games/Schedule', '')
    elif season == '2022-2023':
        team = team[0].replace('\xa0', '').replace(' Games/Schedule (2022-2023)', '')


    games_chart_particular_team = {
                    'plays': [],
                    'team':  team,
                    'links': [],
                    }

    for game_record in game_schedule_records:
        # Check is obtained row is header (for example play of or etc... or not)
        if len(game_record.find_all('td')) != 1:
            single_play_result = get_single_play(game_record.find_all('td'), team, season, league)
        if single_play_result is not None:
            games_chart_particular_team['plays'].append(single_play_result)
            games_chart_particular_team['links'].append(single_play_result[len(single_play_result)-1])

    write_parce_results_in_file(games_chart_particular_team, season)

    return games_chart_particular_team


def pars_play_content(url: str, main_team: str) -> None:
    """Write results of parsing for tournament table in csv file"""

    def decode_string(input_string: str) -> str:
        dict_encoding = {
            '.': '.',
            'w': 'T',
            'I': 'o',
            'U': 't',
            'i': 'a',
            'l': 'l',
            '0': '5',
            '1': '6',
            '2': '8',
            '3': '4',
            '4': '3',
            '5': '0',
            '6': '1',
            '7': '9',
            '8': '2',
            '9': '7',
        }

        input_string_process = list(input_string)
        for l in range(len(input_string_process)):
            input_string_process[l] = dict_encoding[input_string_process[l]]

        return ''.join(input_string_process)

    def team_results_parse(statistics_table_in: bs4.element.Tag) -> Tuple:
        PM2_A2, A2PERC = statistics_table_in.find_all('td')[2].contents[0].split(' ')
        A2PERC = decode_string(A2PERC.replace('(', '').replace(')', '').replace('%', ''))
        PM2, A2 = PM2_A2.split('-')
        PM2 = decode_string(PM2)
        A2 = decode_string(A2)
        PM3_A3, A3PERC = statistics_table_in.find_all('td')[3].contents[0].split(' ')
        A3PERC = decode_string(A3PERC.replace('(', '').replace(')', '').replace('%', ''))
        PM3, A3 = PM3_A3.split('-')
        PM3 = decode_string(PM3)
        A3 = decode_string(A3)
        FTM_FA, FAPERC = statistics_table_in.find_all('td')[4].contents[0].split(' ')
        FAPERC = decode_string(FAPERC.replace('(', '').replace(')', '').replace('%', ''))
        FTM, FA = FTM_FA.split('-')
        FTM = decode_string(FTM)
        FA = decode_string(FA)
        OFF = decode_string(statistics_table_in.find_all('td')[5].contents[0])
        DEF = decode_string(statistics_table_in.find_all('td')[6].contents[0])
        RB = decode_string(statistics_table_in.find_all('td')[7].contents[0])
        AS = decode_string(statistics_table_in.find_all('td')[8].contents[0])
        F = decode_string(statistics_table_in.find_all('td')[9].contents[0])
        RV = decode_string(statistics_table_in.find_all('td')[10].contents[0])
        ST = decode_string(statistics_table_in.find_all('td')[11].contents[0])
        FV = decode_string(statistics_table_in.find_all('td')[12].contents[0])
        AG = decode_string(statistics_table_in.find_all('td')[13].contents[0])
        TO = decode_string(statistics_table_in.find_all('td')[14].contents[0])
        PT = decode_string(statistics_table_in.find_all('td')[15].contents[0])
        RNK = decode_string(statistics_table_in.find_all('td')[16].contents[0])
        return tuple([PM2, A2, A2PERC, PM3, A3, A3PERC,
                      FTM, FA, FAPERC, OFF, DEF, RB, AS,
                      F, RV, ST, FV, AG, TO, PT, RNK])

    def write_results(row, path_in):
        if os.access(path_in, os.F_OK) == False:
            with open(path, 'a', encoding='utf-8') as file_a:
                header = "main_team;league;game;date;local_name;team1;PM2_1;" \
                         "A2_1;A2PERC_1;PM3_1;A3_1;A3PERC_1;FTM_1;FA_1;" \
                         "FAPERC_1;OFF_1;DEF_1;RB_1;AS_1;F_1;RV_1;ST_1;FV_1;AG_1;TO_1;PT_1;RNK_1;" \
                         "team2;PM2_2;A2_2;A2PERC_2;PM3_2;A3_2;A3PERC_2;FTM_2;FA_2;" \
                         "FAPERC_2;OFF_2;DEF_2;RB_2;AS_2;F_2;RV_2;ST_2;FV_2;AG_2;TO_2;PT_2;RNK_2\n"
                file_a.write(header)

        with open(path, 'a', encoding='utf-8') as f:
            items = ''
            for i, item in enumerate(row):
                if i+1 < len(row):
                    items+=f'{str(item)};'
                else:
                    items += f'{str(item)}\n'
            f.write(items)

    def combine_results(results_in: tuple, results_opposite_in: tuple, adds_in: tuple) -> tuple:
        combined_data = []
        combined_data.extend(list(adds_in[:5]))
        # Sometimes succession the tables for in plays in html are not depend on
        # from which team the transition was made so for further correct analysis it is need to
        # swap results of commands and its names.
        if adds_in[0].lower() == adds_in[5].lower() and adds_in[0].lower() != adds_in[6].lower():
            print('Analysed team - {}, first - {}, second - {}'.format(adds_in[0].lower(),
                                                   adds_in[5].lower(),
                                                   adds_in[6].lower()))
            combined_data.extend(list(adds_in[5:6]))
            combined_data.extend(list(results_in))
        else:
            print('Analysed team - {}, first - {}, second - {} so need to swap'.format(adds_in[0].lower(),
                                                   adds_in[5].lower(),
                                                   adds_in[6].lower()))
            combined_data.extend(list(adds_in[6:7]))
            combined_data.extend(list(results_opposite_in))

        if adds_in[0].lower() == adds_in[5].lower() and adds_in[0].lower() != adds_in[6].lower():
            combined_data.extend(list(adds_in[6:7]))
            combined_data.extend(list(results_opposite_in))
        else:
            combined_data.extend(list(adds_in[5:6]))
            combined_data.extend(list(results_in))

        return tuple(combined_data)

    with open(url, 'r', encoding='utf-8') as f:
        response = f.read()

    soup = BeautifulSoup(response, 'lxml')

    team = soup.find('td', class_="my_top_center").find('a').find('span').contents[0]
    game = soup.find('div', id='boxscores').find('div').find_all('span')[1].contents[0].split(':')[0]
    league = soup.find('div', id='boxscores').find('div').find_all('span')[0].contents[0]
    date = soup.find('div', id='boxscores').find('div').find_all('span')[2].contents[0].replace('Date: ', '')
    opposite_team = soup.find_all('td', class_="my_top_center")[1].find('a').find('span').contents[0]
    adds = tuple([main_team, league, game, date, os.path.split(url)[1], team, opposite_team])

    statistics_table = soup.find('tr', class_='my_totalStats')
    results = team_results_parse(statistics_table)
    statistics_table_opposite = soup.find_all('tr', class_='my_totalStats')[1]
    results_opposite = team_results_parse(statistics_table_opposite)

    path = f'./parse_content/plays_results.csv'
    write_results(combine_results(results, results_opposite, adds), path)


if __name__ == '__main__':
    pars_play_content('C:\Python_projects\BasketBallStat\parse_results\Cleveland C\Basketball-Box-Score.asp__quest_mark__Game=2022_1019_14_157-NBA.html', 'Cleveland')
