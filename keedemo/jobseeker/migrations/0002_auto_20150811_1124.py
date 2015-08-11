# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobseeker', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobseeker',
            name='avoir_handicap',
        ),
        migrations.RemoveField(
            model_name='jobseeker',
            name='msg_instantanne',
        ),
        migrations.RemoveField(
            model_name='jobseeker',
            name='permis_conduire',
        ),
        migrations.RemoveField(
            model_name='jobseeker',
            name='titulaire_voitre',
        ),
    ]
