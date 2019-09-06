from .models import FCMToken
from rest_framework import serializers


class FCMTokenSerializer(serializers.ModelSerializer):
    uid = serializers.CharField(required=True)
    token = serializers.CharField(required=False)
    device_id = serializers.CharField(required=False)
    device_type = serializers.CharField(required=False)

    class Meta:
        model = FCMToken
        fields = ['uid', 'token', 'device_id', 'device_type']
