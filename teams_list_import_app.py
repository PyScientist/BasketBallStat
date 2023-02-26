from parse_app import get_content
from proxy_config import random_proxy
from bs4 import BeautifulSoup
import os
import pandas as pd


def parse_teams_list(url, parsing_assingment_path):

    def prepare_local_path(url_in):
        return './parse_results/'+url_in.replace('https://', '').replace('/', '_').replace('.', '_')+'.html'

    local_path = prepare_local_path(url)

    if os.path.isfile(local_path):
        pass
    else:
        get_content(url, local_path, proxies_flag=True, random_proxy=random_proxy)

    with open(local_path, 'r', encoding='utf-8') as f:
        response = f.read()

    soup = BeautifulSoup(response, 'lxml')
    teams_block = soup.find('div', class_='BasketBallTeamDetails')
    team_detail_blocks = teams_block.find_all('div', class_='BasketBallTeamDetailsLine')

    league = soup.find('div', class_='BasketBallTeamTitle').contents[0].replace(" teams", "")
    season = '2022-2023'
    header = ['League', 'Teams', 'Short names', 'Links', 'Season']
    data = []
    for block in team_detail_blocks:
        team = block.find('div', class_='BasketBallTeamName').find('a').contents[0].replace('\n', '').replace('\\','').replace('/','')
        link = block.find('div', class_='BasketBallTeamGames').find('a')['href']
        data.append([league, team, team, link, season])

    new_data_df = pd.DataFrame(data, columns=header)

    if os.path.isfile(parsing_assingment_path):
        df_data_already_exist = pd.read_excel(io=parsing_assingment_path,
                                              engine='openpyxl',
                                              sheet_name='Parse')
        combined_df = pd.concat([df_data_already_exist, new_data_df]).reset_index(drop=True)
        combined_df.drop_duplicates(inplace=True)
    else:
        combined_df = new_data_df

    try:
        with pd.ExcelWriter(parsing_assingment_path, engine='xlsxwriter') as writer:
            combined_df.to_excel(writer, sheet_name='Parse', index=False)
        return f'Parsing assignment have writen to Excel {parsing_assingment_path}'
    except Exception as e:
        return f'While exporting to Excel new parsing assignment an error occurred {e}'


if __name__ == '__main__':
    parse_teams_list('https://www.asia-basket.com/South-Korea/basketball-League-KBL-Teams.aspx',
                     "./Parsing_assignment — копия.xlsx")
