# Generated by Django 5.1.7 on 2025-05-03 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMS_app1', '0008_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(default='user', max_length=20),
        ),
    ]
