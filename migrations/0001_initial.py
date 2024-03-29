# Generated by Django 3.2.23 on 2024-01-26 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Religion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_religion', models.CharField(max_length=10, unique=True)),
                ('nom', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Communaute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_commun', models.CharField(max_length=10, unique=True)),
                ('nom', models.CharField(max_length=60)),
                ('visionaire', models.CharField(max_length=166)),
                ('pasteurs', models.CharField(max_length=166)),
                ('id_religion', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.religion')),
            ],
        ),
    ]
