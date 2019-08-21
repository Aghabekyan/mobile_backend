from .models import User
from rest_framework import viewsets
from .serializers import UserSerializer
from middlewares.auth import FirebaseAuthentication

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import authentication_classes, permission_classes

from helpers.permissions import IsOwner, IsAdmin, IsTest


class UserDetail(viewsets.ViewSet):
    # authentication_classes = ([FirebaseAuthentication])

    # permission_classes_by_action = {'create': [IsAdmin]}
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.request.method == 'GET':
            self.permission_classes = [IsAdmin, IsOwner]
        else:
            self.permission_classes = [IsAdmin, IsOwner]
        return super(UserDetail, self).get_permissions()

    def get_authenticators(self):
        self.authentication_classes = [FirebaseAuthentication]
        return [auth() for auth in self.authentication_classes]

    # @permission_classes(HasPerm1)
    # @authentication_classes([FirebaseAuthentication])
    def retrieve_all(self, request, format=None):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        self.check_object_permissions(self.request, queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        try:
            instance = User.objects.get(pk=pk)
            serializer = UserSerializer(instance)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response('User Does not exist', status=status.HTTP_404_NOT_FOUND)

    # @authentication_classes([FirebaseAuthentication])
    # @permission_classes([HasPerm1])
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
            instance.delete()
        except User.DoesNotExist:
            return Response('User Does not exist', status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)
