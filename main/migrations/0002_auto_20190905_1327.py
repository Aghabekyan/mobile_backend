# Generated by Django 2.2.4 on 2019-09-05 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fcmtoken',
            old_name='user_id',
            new_name='uid',
        ),
    ]
