# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-11 23:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RSR', '0006_auto_20170707_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person_company',
            name='EndDate',
            field=models.DateField(default=11, verbose_name='End Date'),
        ),
        migrations.AlterField(
            model_name='person_company',
            name='StartDate',
            field=models.DateField(default=11, verbose_name='Start Date'),
        ),
    ]
