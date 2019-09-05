from django.db import models


class FCMToken(models.Model):
    uid = models.CharField(max_length=200, primary_key=True)
    token = models.CharField(max_length=200)

    class Meta:
        db_table = 'main_fcm_token'
