from src.browser.scrapping.google_opening import GoogleOpeningPage
import re

def test_login_button():
    google_page = GoogleOpeningPage(headless=True)
    button = str(google_page.get_login_button()[0])
    assert bool(re.search('Login', button))