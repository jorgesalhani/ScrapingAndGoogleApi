from src.browser.scrapping.google_page import GooglePage
import re

def test_login_button():
    google_page = GooglePage(headless=True)
    button = str(google_page.login_button()[0])
    assert bool(re.search('Login', button))