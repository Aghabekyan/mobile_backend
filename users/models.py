from django.db import models


class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)


class User(models.Model):
    uid = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    role = models.ForeignKey(Role, null=True, blank=True, on_delete=models.SET_NULL)

    def is_admin(self):
        return self.role.id == 1


class RezetPassword(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
