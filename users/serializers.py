from .models import User
from rest_framework import serializers


# class UserSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(required=False, allow_blank=True, max_length=100)


#     def create(self, validated_data):
#         return User.objects.create(**validated_data)

#     class Meta:
#         model = User


class UserSerializer(serializers.ModelSerializer):
    uid = serializers.CharField(required=True)
    name = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ['uid', 'name']