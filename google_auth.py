import pygsheets
import pandas as pd
import configparser

# Read authorization data
config = configparser.ConfigParser()
config.read("config.ini")
client_id = config['Goggle_OAuth']['client_id']
client_secret = config['Goggle_OAuth']['client_secret']
# Service file is link on json received during registration of Service Account
service_file = config['Goggle_OAuth']['service_file']


class GoogleSheetsClient:
    """Class to interact with Google sheets"""
    def __init__(self):
        self.google_client = pygsheets.authorize(service_file=service_file)

    def connect_to_particular_gsheet(self, gsheet_name: str) -> pygsheets.spreadsheet.Spreadsheet:
        return self.google_client.open(gsheet_name)

    def connect_to_particular_sheet(self, gsheet_name: str, sheet_name: str) -> pygsheets.worksheet.Worksheet:
        return self.connect_to_particular_gsheet(gsheet_name).worksheet_by_title(sheet_name)

    def set_data_to_particular_sheet(self, gsheet_name: str, sheet_name: str, df: pd.DataFrame) -> None:
        return self.connect_to_particular_sheet(gsheet_name, sheet_name).set_dataframe(df, (1, 1))


if __name__ == '__main__':
    gs_client = GoogleSheetsClient()

    google_sheet = gs_client.connect_to_particular_gsheet('Tables_for_analysis_basketball')
    google_sheet.add_worksheet("results")

    """
    df_test = pd.DataFrame()
    df_test['test'] = [1, 2, 4, 5, 6, 7]
    gs_client.set_data_to_particular_sheet(gsheet_name='Tables_for_analysis_basketball',
                                           sheet_id=0,
                                           df=df_test)
    """