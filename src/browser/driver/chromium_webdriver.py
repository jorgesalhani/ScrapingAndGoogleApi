from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


class ChromiumDriver:
    def __init__(self, headless=False):
        self.driver = None
        self.headless = headless

    @property
    def configure_driver(self) -> Chrome:
        chromium_path = "chrome-win/chrome.exe"
        chromedriver_path = "chromedriver/chromedriver.exe"

        options = Options()
        options.add_argument("start-maximized")
        options.add_argument("--disable-gpu")

        if self.headless:
            options.add_argument("--headless")
            options.add_argument("--ignore-certificate-errors")
            options.add_argument('--log-level=1')
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")

        options.add_experimental_option("detach", True)
        options.binary_location = chromium_path

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager(version='110.0.5481.30').install()),
            options=options
        )
        self.driver = driver
        return driver
