# Generated by Django 3.2.7 on 2021-09-09 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_newuser_about'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newuser',
            name='first_name',
        ),
    ]
