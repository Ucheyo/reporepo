# Generated by Django 4.0.8 on 2022-12-18 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snippet',
            old_name='classID',
            new_name='courseID',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='classID',
            new_name='courseID',
        ),
    ]