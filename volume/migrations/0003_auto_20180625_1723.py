# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-25 17:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0003_auto_20180622_1422'),
        ('compute', '__first__'),
        ('volume', '0002_auto_20180622_1422'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='dbcephquota',
            unique_together=set([('group', 'cephpool')]),
        ),
    ]