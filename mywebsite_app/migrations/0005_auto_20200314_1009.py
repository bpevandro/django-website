# Generated by Django 3.0.4 on 2020-03-14 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite_app', '0004_auto_20200314_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
