# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-04 15:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tvseries', '0005_auto_20171104_1603'),
    ]

    operations = [
        migrations.RenameField(
            model_name='writer',
            old_name='W_name',
            new_name='Writer',
        ),
        migrations.RenameField(
            model_name='writer',
            old_name='W_pic',
            new_name='Writer_pic',
        ),
    ]
