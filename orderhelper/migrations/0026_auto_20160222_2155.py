# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-22 19:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orderhelper', '0025_auto_20160222_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comanda',
            name='data',
            field=models.DateField(default=datetime.datetime(2016, 2, 22, 19, 55, 12, 776190, tzinfo=utc), verbose_name='Data'),
        ),
    ]
