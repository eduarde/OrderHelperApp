# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-21 21:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderhelper', '0019_comanda'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcomanda',
            name='numar_unic_comanda',
            field=models.IntegerField(null=True, verbose_name='Numar comanda'),
        ),
        migrations.AlterField(
            model_name='subcomanda',
            name='numar_curent',
            field=models.IntegerField(null=True, verbose_name='Numar Curent'),
        ),
    ]
