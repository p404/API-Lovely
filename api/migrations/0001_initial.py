# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-14 21:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('beds', models.IntegerField()),
                ('baths', models.IntegerField()),
                ('address', models.CharField(max_length=120)),
                ('provider_name', models.CharField(max_length=120)),
            ],
            options={
                'ordering': ('price',),
            },
        ),
    ]
