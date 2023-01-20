import httplib2
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from src.google_services.google_oauth import GoogleOAuth


class GoogleUserInfo(GoogleOAuth):
    def __init__(self):
        super().__init__()
        super().authenticate()

    def user_info(self):
        try:
            service = build(
                serviceName='oauth2', version='v2', credentials=self.creds)
            user_info = service.userinfo().get().execute()
            if user_info and user_info.get('id'):
                return {
                    'email': user_info['email'],
                    'name': user_info['name']
                }
        except HttpError as err:
            raise err

