# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-21 18:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderhelper', '0002_solicitant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proiect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Denumire')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descriere')),
                ('telephone', models.CharField(blank=True, max_length=10, null=True, verbose_name='Telefon')),
            ],
        ),
    ]
