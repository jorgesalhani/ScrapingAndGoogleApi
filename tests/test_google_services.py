import os
from src.google_services.google_sheets import GoogleSheets
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
ID_SHEET_TEST0 = os.getenv('ID_SHEET_TEST0')
TAB_NAME_SHEET_TEST0 = os.getenv('TAB_NAME_SHEET_TEST0')

def test_get_all_content():
    data = GoogleSheets().get_all_data(
        ID_SHEET_TEST0,
        TAB_NAME_SHEET_TEST0
    )
    assert data == [['TesteA1']]