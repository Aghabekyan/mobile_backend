from django.db import models


class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=500)
    role = models.ForeignKey(Role, null=True, blank=True, on_delete=models.SET_NULL)


    # def create(self, values):
    #     self.username = values.get("username")
    #     self.email = values.get("email").lower()
    #     self.password = generate_password_hash(values.get("password"))
    #
    #     self.store()
    #
    #     # self.send_verification_email()
    #
    #     return self


    def is_admin(self):
        if self.role is not None:
            return self.role.id == 1
        else:
            return False


class ResetPassword(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
