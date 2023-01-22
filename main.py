from src.google_services.google_sheets import GoogleSheets
from src.google_services.google_user_info import GoogleUserInfo
from src.browser.scrapping.google_page import GooglePage

if __name__ == '__main__':
    data = GoogleSheets().get_all_data(
        '1ivsK84W3KCIyb7_YOF9SSXkCl_vlUmvgMPr-ip15qhE',
        "'ABA1'"
    )
    user = GoogleUserInfo().user_info()
    print(user)
    print(data)

    google_page = GooglePage()
    button = google_page.login_button()

    print(button)