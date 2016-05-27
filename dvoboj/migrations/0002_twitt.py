# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-26 12:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvoboj', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Twitt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=1024)),
                ('url', models.URLField(blank=True, null=True)),
                ('content', models.CharField(blank=True, max_length=256, null=True)),
                ('timestamp', models.DateTimeField()),
                ('isVideo', models.BooleanField(default=False)),
                ('isFoto', models.BooleanField(default=False)),
                ('content_url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
