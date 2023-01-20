from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from src.google_services.google_oauth import GoogleOAuth


class GoogleSheets(GoogleOAuth):
    def __init__(self):
        super().__init__()
        super().authenticate()
        self.google_spreadsheet = None
        try:
            service = build('sheets', 'v4', credentials=self.creds)
            self.google_spreadsheet = service.spreadsheets()
        except HttpError as err:
            raise err

    def get_all_data(self, spreadsheet_id: str, tab_name: str):
        try:
            sheet = self.google_spreadsheet.values().get(
                spreadsheetId=spreadsheet_id,
                range=tab_name,
                majorDimension='ROWS'
            ).execute()

            data = sheet['values']
        except HttpError as err:
            raise err
        return data


