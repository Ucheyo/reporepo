# Generated by Django 4.0.8 on 2023-01-09 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0003_alter_student_classesattended'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='post',
            field=models.TextField(blank=True, default='', max_length=100),
        ),
    ]
