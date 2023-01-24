import os

from src.google_services.google_sheets import GoogleSheets
from src.google_services.google_user_info import GoogleUserInfo
from src.browser.scrapping.google_page import GooglePage
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
ID_SHEET_TEST0 = os.getenv('ID_SHEET_TEST0')
TAB_NAME_SHEET_TEST0 = os.getenv('TAB_NAME_SHEET_TEST0')

if __name__ == '__main__':
    data = GoogleSheets().get_all_data(
        ID_SHEET_TEST0,
        TAB_NAME_SHEET_TEST0
    )
    print(data)
