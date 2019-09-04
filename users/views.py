from .models import User, ResetPassword
from rest_framework import viewsets
from .serializers import UserSerializer
from middlewares.auth import FirebaseAuthentication
from rest_framework.response import Response
from rest_framework import status
from helpers.permissions import IsAdmin, IsOwnerOrAdmin
from django.core.mail import send_mail
from django.conf import settings
import uuid

class UserDetail(viewsets.ViewSet):

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        self.permission_classes = []
        if self.action == 'retrieve_all':
            self.permission_classes = [IsAdmin]
        if self.action == 'retrieve':
            self.permission_classes = [IsOwnerOrAdmin]
        if self.action == 'create':
            self.permission_classes = []
        if self.action == 'update':
            self.permission_classes = [IsOwnerOrAdmin]
        if self.action == 'partial_update':
            self.permission_classes = [IsOwnerOrAdmin]
        if self.action == 'destroy':
            self.permission_classes = [IsOwnerOrAdmin]
        return [permission() for permission in self.permission_classes]

    def get_authenticators(self):
        self.authentication_classes = [FirebaseAuthentication]
        return [auth() for auth in self.authentication_classes]

    def retrieve_all(self, request, format=None):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        try:
            instance = User.objects.get(pk=pk)
            serializer = UserSerializer(instance)
            self.check_object_permissions(self.request, instance)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response('User Does not exist', status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            instance = User.objects.get(pk=pk)
            self.check_object_permissions(self.request, instance)
        except User.DoesNotExist:
            return Response('User Does not exist', status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        try:
            instance = User.objects.get(pk=pk)
            self.check_object_permissions(self.request, instance)
        except User.DoesNotExist:
            return Response('User Does not exist', status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            instance = User.objects.get(pk=pk)
            self.check_object_permissions(self.request, instance)
            instance.delete()
        except User.DoesNotExist:
            return Response('User Does not exist', status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def reset_password(self, request):
        data = request.data
        token = uuid.uuid4().hex

        user = User.objects.get(pk=data['uid'])
        ResetPassword.objects.create(uid=user, token = token)

        subject = 'Thank you for registering to our site'
        message = f"<h1>Please click this link</h1> http://127.0.0.1/api/v1/users/reset_password/confirm?uid={data['uid']}&token={token}"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['s.aghabekyan@yandex.ru',]
        send_mail( subject=subject, html_message=message, from_email=email_from, recipient_list=recipient_list, message=None )
        
        return Response(data, status=status.HTTP_200_OK)

    def change_password(self, request):
        data = request.data

        user = User.objects.get(pk=data['uid'])

        today_date = datetime.today()
        actual_date = today_date - timedelta(days=2)

        ResetPassword.objects.filter(uid=user, token=token, created__lte=actual_date)

        if data['new_password_1'] == data['new_password_2']:
            user = auth.update_user(
                uid,
                password=data['new_password_1']
            )

        return Response(data, status=status.HTTP_200_OK)
