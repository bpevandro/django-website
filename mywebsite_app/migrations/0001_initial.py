# Generated by Django 3.0.4 on 2020-03-14 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=200)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('link_to_project', models.TextField(max_length=200)),
            ],
        ),
    ]
