from .models import User
from rest_framework import viewsets
from .serializers import UserSerializer
from middlewares.auth import ExampleAuthentication


class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = (ExampleAuthentication,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
