from django.conf import settings
import jwt
import datetime

class JWTManager:

    @staticmethod
    def access_jwt(user_id):
        return jwt.encode({'user_id': user_id,
                           'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=settings.JWT_ACCESS_EXP_SECONDS)},
                           settings.JWT_SECRET,
                           algorithm=settings.JWT_ALGORITHM)

    @staticmethod
    def refresh_jwt(user_id):
        return jwt.encode({'user_id': user_id,
                           'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=settings.JWT_REFRESH_EXP_SECONDS)},
                           settings.JWT_SECRET,
                           algorithm=settings.JWT_ALGORITHM)

    @staticmethod
    def decode(token):
        return jwt.encode(token,
                          settings.JWT_SECRET,
                          algorithm=settings.JWT_ALGORITHM)
