# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-16 23:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='system',
            new_name='graphics',
        ),
    ]
