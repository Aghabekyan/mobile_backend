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

class ExampleAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        print(3333333)
        username = request.META.get('X_USERNAME') # get the username request header
        print(username)
        if not username: # no username passed in request headers
            raise exceptions.AuthenticationFailed('No such user')

        try:
            user = User.objects.get(username=username) # get the user
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user') # raise exception if user does not exist 

        return (user, None) # authentication successful