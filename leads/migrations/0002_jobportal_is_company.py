# Generated by Django 4.0.5 on 2023-04-08 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobportal',
            name='is_company',
            field=models.BooleanField(default=False),
        ),
    ]