# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-27 11:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nodes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nodes', models.CharField(max_length=512)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('routes', models.CharField(max_length=1000)),
                ('spath', models.CharField(max_length=10000000)),
            ],
        ),
    ]
