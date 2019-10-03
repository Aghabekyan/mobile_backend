from django.conf import settings
from rest_framework import exceptions
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from werkzeug.security import check_password_hash
from users.models import User
from users.serializers import UserLoginSerializer
from rest_framework.views import APIView
import datetime
from helpers.utils import JWTManager

from rest_framework.response import Response

class UserLoginView(APIView):
    # permission_classes = (AllowAny,)

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                email = request.data['email']
                email = email.lower()
                password = request.data['password']
                user = User.objects.get(email=email)
                if user:
                    if user.password and check_password_hash(user.password, password):
                        refresh_token = JWTManager.refresh_jwt(user.id)
                        access_token = JWTManager.access_jwt(user.id)
                        user_data = {}
                        user_data['user_id'] = user.id
                        user_data['refresh_token'] = refresh_token
                        user_data['access_token'] = access_token
                        return Response(user_data,
                                        status=status.HTTP_200_OK)
                    else:
                        return Response('Message.WRONG_CREDENTIALS',
                                        status=status.HTTP_422_UNPROCESSABLE_ENTITY)
                else:
                    return Response('message=Message.USER_NOT_FOUND',
                                    status=status.HTTP_200_OK)

            except exceptions.APIException:
                return Response('message=Message.ERROR',
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class UserLogoutView(APIView):
    # permission_classes = (IsAuthenticated,)

    def post(self, request):
        return Response('Message.SUCCESS',
                        status=status.HTTP_200_OK)
        # try:
        #     jwt = JWTAuthentication()
        #     header = jwt.get_header(request)
        #     raw_token = jwt.get_raw_token(header)
        #     payload = AccessToken(raw_token).payload
        #     cache.set(payload['token_type'] + '_' + payload['jti'], 1)
        #
        #     return Response(message=Message.SUCCESS,
        #                     status_code=status.HTTP_200_OK)
        #
        # except exceptions.APIException:
        #     return Response(message=Message.ERROR,
        #                     status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        #                     success=False)
        # except TokenError:
        #     return Response(message=Message.SUCCESS,
        #                     status_code=status.HTTP_200_OK)
        # except InvalidToken:
        #     return Response(message=Message.SUCCESS,
        #                     status_code=status.HTTP_200_OK)
