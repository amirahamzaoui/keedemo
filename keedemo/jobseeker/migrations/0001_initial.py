# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CvInfoPro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titre_profil', models.CharField(max_length=200)),
                ('niveau_etudes', models.CharField(max_length=200)),
                ('nbre_exp', models.CharField(max_length=200)),
                ('salaire_actuel', models.CharField(max_length=200)),
                ('situation_professionelle', models.CharField(max_length=200)),
                ('disponibilite', models.CharField(max_length=200)),
                ('salaire_min_souhaite', models.CharField(max_length=200)),
                ('metiers', models.CharField(max_length=200)),
                ('secteur_activite', models.CharField(max_length=200)),
                ('type_poste', models.CharField(max_length=200)),
                ('lieu_travail', models.CharField(max_length=200)),
                ('mobilite', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Jobseeker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('prenom', models.CharField(max_length=200)),
                ('nom', models.CharField(max_length=200)),
                ('sexe', models.CharField(max_length=1, choices=[(b'F', b'Feminin'), (b'M', b'Masculin')])),
                ('date_naissance', models.DateField(auto_now=True)),
                ('etat_civil', models.CharField(max_length=1, choices=[(b'Celibataire', b'Celibataire'), (b'Marie', b'Marie')])),
                ('nationalite', models.CharField(max_length=200, blank=True)),
                ('adresse', models.CharField(max_length=200, blank=True)),
                ('code_postal', models.CharField(max_length=200, blank=True)),
                ('telephone', models.CharField(max_length=8, blank=True)),
                ('msg_instantanne', models.CharField(max_length=200, blank=True)),
                ('permis_conduire', models.BooleanField(default=False)),
                ('titulaire_voitre', models.BooleanField(default=False)),
                ('avoir_handicap', models.BooleanField(default=False)),
            ],
        ),
    ]
