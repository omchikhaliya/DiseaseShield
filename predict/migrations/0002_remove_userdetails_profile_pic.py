# Generated by Django 4.1.5 on 2024-01-18 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='profile_pic',
        ),
    ]
