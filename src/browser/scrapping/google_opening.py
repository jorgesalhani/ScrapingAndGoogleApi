from src.browser.driver.chromium_webdriver import ChromiumDriver
from bs4 import BeautifulSoup


class GoogleOpeningPage(ChromiumDriver):
    def __init__(self, headless=False):
        super().__init__(headless=headless)
        self.driver = super().configure_driver

    def get_login_button(self):
        self.driver.get("https://www.google.com")
        soup_google = BeautifulSoup(self.driver.page_source, features="html.parser")
        login_button = soup_google.find_all(
            lambda tag: len(tag.find_all()) == 0 and "login" in tag.text
        )
        self.driver.close()
        return login_button



