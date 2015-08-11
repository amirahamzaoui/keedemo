from django.db import models

# Create your models here.
class Jobseeker (models.Model):
    SEXE_GENDER = (
    ('F', 'Feminin'),
    ('M', 'Masculin'),
)
    ETAT_CIVIL_CHOICES = (
    ('Celibataire', 'Celibataire'),
    ('Marie', 'Marie'),
)
    prenom = models.CharField(max_length=200)
    nom = models.CharField(max_length=200)
    sexe = models.CharField(choices=SEXE_GENDER, max_length=1)
    date_naissance = models.DateField(auto_now=True)
    etat_civil = models.CharField(choices=ETAT_CIVIL_CHOICES, max_length=22)
    nationalite = models.CharField(max_length=200, blank = True)
    adresse = models.CharField(max_length=200,blank = True)
    code_postal = models.CharField(blank = True,max_length = 200)
    telephone = models.CharField(max_length=8, blank = True)
    msg_instantanne = models.CharField(max_length = 200,blank = True)
    permis_conduire = models.BooleanField(default = False)
    titulaire_voitre = models.BooleanField(default = False)
    avoir_handicap =  models.BooleanField(default = False)

    def __str__(self):              # __unicode__ on Python 2
        return self.nom

class CvInfoPro (models.Model):
    titre_profil = models.CharField(max_length=200)
    niveau_etudes = models.CharField(max_length=200)
    nbre_exp = models.CharField(max_length=200)
    salaire_actuel = models.CharField(max_length=200)
    situation_professionelle = models.CharField(max_length=200)
    disponibilite = models.CharField(max_length=200)
    salaire_min_souhaite = models.CharField(max_length=200)
    metiers = models.CharField(max_length=200)
    secteur_activite = models.CharField(max_length=200)
    type_poste = models.CharField(max_length=200)
    lieu_travail = models.CharField(max_length=200)
    mobilite = models.CharField(max_length=200)

    def __str__(self):              # __unicode__ on Python 2
        return self.titre_profil