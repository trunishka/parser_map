# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 10:58
from __future__ import unicode_literals

from django.db import migrations, models
import ip_parse.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compromized_IP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255, unique=True)),
                ('appear_date', models.CharField(max_length=20)),
                ('ip_adress', models.CharField(max_length=15)),
                ('as_number', models.CharField(blank=True, max_length=15, null=True, verbose_name=ip_parse.models.Subnet)),
                ('malware_type', models.CharField(max_length=255)),
                ('geom', models.CharField(max_length=99999)),
            ],
        ),
        migrations.CreateModel(
            name='Subnet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('as_number', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=255)),
                ('organization', models.CharField(max_length=255)),
                ('range_of_ip', models.CharField(max_length=20)),
            ],
        ),
    ]
