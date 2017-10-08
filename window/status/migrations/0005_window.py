# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-08 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0004_auto_20171008_0922'),
    ]

    operations = [
        migrations.CreateModel(
            name='Window',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('state', models.CharField(max_length=5)),
            ],
        ),
    ]
