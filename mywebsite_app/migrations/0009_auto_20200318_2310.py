# Generated by Django 3.0.4 on 2020-03-18 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite_app', '0008_auto_20200318_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='github_link',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='other_link',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
