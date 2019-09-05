from users.models import User, ResetPassword
from rest_framework import viewsets
from middlewares.auth import FirebaseAuthentication
from rest_framework.response import Response
from rest_framework import status
from helpers.permissions import IsOwner
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime, timedelta
from firebase_admin import auth
import uuid


class UserPasswordDetail(viewsets.ViewSet):

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        self.permission_classes = []
        if self.action == 'reset_password':
            self.permission_classes = [IsOwner]
        if self.action == 'change_password':
            self.permission_classes = [IsOwner]
        return [permission() for permission in self.permission_classes]

    def get_authenticators(self):
        self.authentication_classes = [FirebaseAuthentication]
        return [auth() for auth in self.authentication_classes]

    def reset_password(self, request):
        data = request.data
        token = uuid.uuid4().hex
        user = User.objects.get(pk=data['uid'])
        ResetPassword.objects.create(uid=user, token=token)
        subject = 'Thank you for registering to our site'
        message = f"<h1>Please click this link</h1> http://127.0.0.1/api/v1/users/reset_password/confirm?uid={data['uid']}&token={token}"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['s.aghabekyan@yandex.ru', ]
        send_mail(subject=subject, html_message=message, from_email=email_from, recipient_list=recipient_list, message=None)
        return Response(data, status=status.HTTP_200_OK)

    def change_password(self, request):
        data = request.data
        user = User.objects.get(pk=data['uid'])
        today_date = datetime.today()
        actual_date = today_date - timedelta(days=2)
        ResetPassword.objects.filter(uid=user, token=data['token'], created__lte=actual_date)

        if data['new_password_1'] == data['new_password_2']:
            user = auth.update_user(
                data['uid'],
                password=data['new_password_1']
            )

        return Response(data, status=status.HTTP_200_OK)
