# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-27 08:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orderhelper', '0028_auto_20160227_0919'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proiect',
            name='telefon',
        ),
        migrations.AlterField(
            model_name='comanda',
            name='data',
            field=models.DateField(default=datetime.datetime(2016, 2, 27, 8, 50, 23, 253847, tzinfo=utc), verbose_name='Data'),
        ),
    ]