# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfinal', '0006_auto_20150520_1550'),
    ]

    operations = [
        migrations.CreateModel(
            name='event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=None, max_length=250)),
                ('date', models.DateField(default=None)),
                ('time', models.TimeField(default=None)),
                ('description', models.TextField()),
                ('picked', models.BooleanField(default=False)),
                ('price', models.FloatField(default=None, max_length=100.0)),
                ('kind', models.CharField(default=None, max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='activity',
        ),
    ]
