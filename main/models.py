from django.db import models


class DeviceType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'main_device_type'


class FCMToken(models.Model):
    uid = models.CharField(max_length=200, primary_key=True)
    token = models.CharField(max_length=200)
    device_id = models.CharField(max_length=200)
    device_type = models.ForeignKey(DeviceType, on_delete=models.CASCADE)

    class Meta:
        db_table = 'main_fcm_token'
