# Generated by Django 3.2.23 on 2024-01-26 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='communaute',
            name='id_commun',
        ),
        migrations.RemoveField(
            model_name='religion',
            name='id_religion',
        ),
    ]
