# Generated by Django 4.1 on 2022-09-17 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('csm_app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='user',
        ),
    ]
