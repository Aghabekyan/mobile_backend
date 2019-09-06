from main.models import FCMToken
from rest_framework import viewsets
from main.serializers import FCMTokenSerializer
from middlewares.auth import FirebaseAuthentication
from rest_framework.response import Response
from rest_framework import status
from helpers.permissions import IsOwner


class FCMTokenDetail(viewsets.ViewSet):

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        self.permission_classes = [IsOwner]
        # if self.action == 'create':
        #     self.permission_classes = [IsOwner]
        # if self.action == 'destroy':
        #     self.permission_classes = [IsOwner]
        return [permission() for permission in self.permission_classes]

    def get_authenticators(self):
        self.authentication_classes = [FirebaseAuthentication]
        return [auth() for auth in self.authentication_classes]

    def create(self, request):
        serializer = FCMTokenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            instance = FCMToken.objects.get(pk=pk)
            self.check_object_permissions(self.request, instance)
            instance.delete()
        except FCMToken.DoesNotExist:
            return Response('FCM Token Does not exist', status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)
