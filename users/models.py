from django.db import models


class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)


class User(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    role = models.ForeignKey(Role, null=True, blank=True, on_delete=models.SET_NULL)
