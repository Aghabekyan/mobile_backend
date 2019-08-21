from users.models import User
from rest_framework import authentication
from rest_framework import exceptions
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

class FirebaseAuthentication(authentication.BaseAuthentication):

    def _get_jwt_token(self, request):
        token = request.headers['Authorization'].split(' ')[-1]
        return token

    def _get_uid_from_token(self, token):
        decoded_token = auth.verify_id_token(token)
        return decoded_token['uid']

    def _get_user_from_uid(self, uid):
        user = auth.get_user(uid)
        return user

    def authenticate(self, request):
        print("Firebase auth")
        if (not len(firebase_admin._apps)):
            cred = credentials.Certificate("./key.json")
            firebase_admin.initialize_app(cred)
        try:
            token = self._get_jwt_token(request)
            uid = self._get_uid_from_token(token)
            if request.method != "POST":
                user = User.objects.get(uid=uid) # get the user
            else:
                user = None
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')
        except ValueError as e:
            raise exceptions.AuthenticationFailed({"error": str(e)})
        except:
            raise exceptions.AuthenticationFailed('Unauthorized')


        # if request.method == "POST":
        #     try:
        #         user = User.objects.get(uid=uid) # get the user
        #     except User.DoesNotExist:
        #         u = User.objects.create(uid=uid, name='sullivan')
        #         u.save()
        #     except:
        #         raise exceptions.AuthenticationFailed('Unauthorized') 



        return (user, None) # authentication successful