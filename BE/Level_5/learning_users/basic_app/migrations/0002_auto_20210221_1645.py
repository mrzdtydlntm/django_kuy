# Generated by Django 3.1.6 on 2021-02-21 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='profil_pic',
            new_name='profile_pic',
        ),
    ]
