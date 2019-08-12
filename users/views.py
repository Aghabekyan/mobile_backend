from .models import User
from rest_framework import viewsets
from .serializers import UserSerializer
from middlewares.auth import FirebaseAuthentication


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserDetail(viewsets.ViewSet):
    authentication_classes = [FirebaseAuthentication]

    def retrieve_all(self, request, format=None):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        try:
            instance = User.objects.get(pk=pk)
            serializer = UserSerializer(instance)
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
