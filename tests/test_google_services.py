from src.google_services.google_sheets import GoogleSheets


def test_get_all_content():
    data = GoogleSheets().get_all_data(
        '1ivsK84W3KCIyb7_YOF9SSXkCl_vlUmvgMPr-ip15qhE',
        "'ABA1'"
    )
    assert data == [['TesteA1']]