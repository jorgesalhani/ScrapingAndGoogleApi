from src.browser.driver.chromium_webdriver import ChromiumDriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


class GooglePage(ChromiumDriver):
    def __init__(self, headless=False):
        super().__init__(headless=headless)
        self.driver = super().configure_driver

    def login_button(self):
        self.driver.get("https://www.google.com")
        soup_google = BeautifulSoup(self.driver.page_source, features="html.parser")
        login_button = soup_google.find_all(
            lambda tag: len(tag.find_all()) == 0 and "login" in tag.text
        )
        if len(login_button) != 1:
            return
        selenium_element = self.driver.find_element(By.PARTIAL_LINK_TEXT, 'login')
        selenium_element.click()

        self.driver.close()
        return login_button


