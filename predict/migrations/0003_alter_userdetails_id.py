# Generated by Django 4.1.5 on 2024-01-19 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0002_remove_userdetails_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]