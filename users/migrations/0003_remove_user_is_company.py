# Generated by Django 4.0.5 on 2023-04-11 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_is_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_company',
        ),
    ]
