# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-04 10:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvseries', '0004_movie_is_favourite'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='M_logo',
            field=models.CharField(default='pqr', max_length=1000),
        ),
        migrations.AddField(
            model_name='writer',
            name='W_pic',
            field=models.CharField(default='abc', max_length=1000),
        ),
    ]
