# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-27 07:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        ('orderhelper', '0027_auto_20160224_1951'),
    ]

    operations = [
        migrations.AddField(
            model_name='proiect',
            name='group',
            field=models.ManyToManyField(related_name='proiects', to='auth.Group'),
        ),
        migrations.AlterField(
            model_name='comanda',
            name='data',
            field=models.DateField(default=datetime.datetime(2016, 2, 27, 7, 19, 50, 781757, tzinfo=utc), verbose_name='Data'),
        ),
    ]