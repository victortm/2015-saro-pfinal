# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfinal', '0014_activitie_cost'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('name', models.CharField(max_length=32, serialize=False, primary_key=True)),
                ('activity', models.ManyToManyField(to='pfinal.activitie', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='activitie',
            name='pickdate',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
