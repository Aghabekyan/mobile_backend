from users.models import User
from rest_framework import authentication
from rest_framework import exceptions
import jwt

class JWTAuthentication(authentication.BaseAuthentication):

    def _get_jwt_token(self, request):
        token = request.headers['Authorization'].split(' ')[-1]
        return token

    def authenticate(self, request):
        print("JWT Authentication")
        user = None
        try:
            token = self._get_jwt_token(request)
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            uid = payload['user_id']
            user = User.objects.get(uid=uid)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')
        except Exception as e:
            raise exceptions.AuthenticationFailed({"error": str(e)})
            # raise exceptions.AuthenticationFailed('Unauthorized')

        return (user, None)  # authentication successful
