# Generated by Django 2.2.4 on 2019-08-30 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_rezetpassword'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RezetPassword',
            new_name='ResetPassword',
        ),
    ]
