# Generated by Django 3.0.4 on 2020-03-19 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite_app', '0009_auto_20200318_2310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='link',
        ),
    ]
