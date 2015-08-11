# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobseeker', '0002_auto_20150811_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobseeker',
            name='avoir_handicap',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='msg_instantanne',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='permis_conduire',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='titulaire_voitre',
            field=models.BooleanField(default=False),
        ),
    ]
