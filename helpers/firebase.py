from django.conf import settings
from firebase_admin import _apps, credentials, auth, initialize_app


class FirebaseUserManager:
    _token = None
    _uid = None

    def __init__(self, token):
        self._token = token
        if (not len(_apps)):
            cred = credentials.Certificate(settings.FIREBASE_CERTIFICATE)
            initialize_app(cred)

    def get_user(self):
        if self._uid is None:
            self.get_uid()
        user = auth.get_user(self._uid)
        return user

    def get_uid(self):
        decoded_token = auth.verify_id_token(self._token)
        self._uid = decoded_token['uid']
        return self._uid
