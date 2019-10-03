from users.models import User
from rest_framework import viewsets
from users.serializers import UserCreateSerializer
from rest_framework.response import Response
from rest_framework import status
from helpers.permissions import IsAdmin, IsOwnerOrAdmin
from rest_framework.views import APIView
import jwt
from werkzeug.security import generate_password_hash

class UserCreateView(APIView):
    # permission_classes = (AllowAny,)

    def post(self, request):

        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['password'] = generate_password_hash(serializer.validated_data['password'])
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


