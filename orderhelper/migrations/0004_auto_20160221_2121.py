# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-21 19:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orderhelper', '0003_proiect'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Solicitant',
            new_name='Person',
        ),
        migrations.RenameModel(
            old_name='Proiect',
            new_name='Project',
        ),
    ]
