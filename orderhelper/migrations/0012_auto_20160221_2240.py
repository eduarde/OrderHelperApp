# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-21 20:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderhelper', '0011_auto_20160221_2237'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcomanda',
            name='intarziere',
            field=models.IntegerField(null=True, verbose_name='Intarziere'),
        ),
        migrations.AddField(
            model_name='subcomanda',
            name='link',
            field=models.URLField(null=True, verbose_name='Link'),
        ),
        migrations.AddField(
            model_name='subcomanda',
            name='pret',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9, null=True, verbose_name='Cantitate'),
        ),
        migrations.AlterField(
            model_name='subcomanda',
            name='data_livrare',
            field=models.DateField(null=True, verbose_name='Data livrare'),
        ),
    ]
