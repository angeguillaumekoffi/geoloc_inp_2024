# Generated by Django 5.0.1 on 2024-01-06 14:55

import datetime
import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Historique',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('vehicule', models.CharField(max_length=20)),
                ('position', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('date_heure', models.DateTimeField(default=datetime.datetime(2024, 1, 6, 15, 55, 48, 412473))),
            ],
            options={
                'db_table': 'historique',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Vehicule',
            fields=[
                ('immatriculation', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='immatriculation')),
                ('marque', models.CharField(max_length=100)),
                ('couleur', models.CharField(max_length=50)),
                ('modele', models.CharField(max_length=100, verbose_name='modele')),
                ('position', django.contrib.gis.db.models.fields.PointField(null=True, srid=4326)),
            ],
            options={
                'db_table': 'vehicule',
                'managed': False,
            },
        ),
    ]
