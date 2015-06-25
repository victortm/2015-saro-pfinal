# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfinal', '0013_auto_20150522_0832'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitie',
            name='cost',
            field=models.CharField(max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
    ]
