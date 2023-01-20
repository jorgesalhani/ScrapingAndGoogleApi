from src.google_services.google_sheets import GoogleSheets

if __name__ == '__main__':
    data = GoogleSheets().get_all_data(
        '1ivsK84W3KCIyb7_YOF9SSXkCl_vlUmvgMPr-ip15qhE',
        "'ABA1'"
    )
    print(data)