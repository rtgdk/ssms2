# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-08-21 19:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssms', '0009_grub_spot_signing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grub',
            name='spot_signing',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=6),
        ),
    ]
