# Generated by Django 4.2.2 on 2023-06-07 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Home',
            new_name='WelcomeMessages',
        ),
    ]
