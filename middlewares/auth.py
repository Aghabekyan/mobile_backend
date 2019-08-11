class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print(1111111)
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        
        response = self.get_response(request)
        print(222222222)

        # Code to be executed for each request/response after
        # the view is called.

        return response



from users.models import User
from rest_framework import authentication
from rest_framework import exceptions
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

class ExampleAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        print(3333333)

        # cred = credentials.Certificate("nareks_key.json")
        cred = credentials.Certificate("./key.json")
        firebase_admin.initialize_app(cred)
        user = auth.get_user('DCET87AVove5lLCpLONpB3N39DS2')
        import pdb
        pdb.set_trace()
        # print(dir(user))
        try:
            decoded_token = auth.verify_id_token('eyJhbGciOiJSUzI1NiIsImtpZCI6IjcyODRlYTZiNGZlZDBmZDc1MzE4NTg2NDZmZDYzNjE1ZGQ3YTIyZjUiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoibmFyZWsiLCJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vdGVzdGFwcC1hNzg1OSIsImF1ZCI6InRlc3RhcHAtYTc4NTkiLCJhdXRoX3RpbWUiOjE1NjUyNzAxNDEsInVzZXJfaWQiOiJPZUc4NFY3a0hZZVZoYzIxOGJQNmpUV0FsVGwyIiwic3ViIjoiT2VHODRWN2tIWWVWaGMyMThiUDZqVFdBbFRsMiIsImlhdCI6MTU2NTI3MDE0MSwiZXhwIjoxNTY1MjczNzQxLCJlbWFpbCI6Im5hcmVrc2ltb255YW45NEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZW1haWwiOlsibmFyZWtzaW1vbnlhbjk0QGdtYWlsLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.gdWJsra57XjPlmtQoX69QbcmzSmRTYRNxKcvJQ5owu9k1sM4iSgZ_WFoKZiqm3qrboDUmkGPVMk_mDEhMz9xuvE6pGQEQojJkLOAz3EeSgzV-xRKE_zkgLcHOXY5l74xP2AI7bWcH7DxrwwirKa4_h8etKN61Nso4ucikzGox2WAJpLOFmYpnXGKsCALe0iFKNAW9W4PIuAyIWUve0t78LrZ-5Pq28mJza5WnBuRQ7aQybd2DyHUrlzPZ-zFL3kkwoXkaFVFfqibpgcVmhYqSGgpiJ7MdatwrGGK4zKyEftyN0WkP1A1DGYfIPahO8VdrWhiTyxTzYjEZlO3aDnWjA')
            uid = decoded_tokento_dict()
            user = User.objects.get(username=uid) # get the user
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user') # raise exception if user does not exist 
        except:
            raise exceptions.AuthenticationFailed('Unauthorized') # raise exception if user does not exist 

        return (user, None) # authentication successful