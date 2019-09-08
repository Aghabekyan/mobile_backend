from users.models import User
from rest_framework import authentication
from rest_framework import exceptions
from helpers.firebase import FirebaseUserManager


class FirebaseAuthentication(authentication.BaseAuthentication):

    def _get_jwt_token(self, request):
        token = request.headers['Authorization'].split(' ')[-1]
        return token

    def authenticate(self, request):
        print("Firebase auth")
        user = None
        try:
            token = self._get_jwt_token(request)
            firebaseUserManager = FirebaseUserManager(token)
            uid = firebaseUserManager.get_uid()
            if request.method != "POST":
                user = User.objects.get(uid=uid)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')
        except Exception as e:
            raise exceptions.AuthenticationFailed({"error": str(e)})
            # raise exceptions.AuthenticationFailed('Unauthorized')

        return (user, None)  # authentication successful
