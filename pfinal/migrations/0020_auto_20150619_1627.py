# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfinal', '0019_remove_activitie_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myacc',
            name='activity',
            field=models.ManyToManyField(to='pfinal.activitie'),
            preserve_default=True,
        ),
    ]
