from django.db import models

# Create your models here.
from django.db import models

class Salle(models.Model):
    nom = models.CharField(max_length=100)
    type_salle = models.CharField(max_length=50, choices=[
        ('CM', 'Cours Magistral'),
        ('TD', 'Travaux Dirigés'),
        ('TP', 'Travaux Pratiques'),
        ('REUNION', 'Réunion'),
        ('ETUDE', 'Étude'),
    ])
    capacite = models.IntegerField()

class MaterielPedagogique(models.Model):
    nom = models.CharField(max_length=100)
    quantite = models.IntegerField()
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE)

class Classe(models.Model):
    nom = models.CharField(max_length=100)
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE)

class Enseignant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()

class Cours(models.Model):
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    date = models.DateField()
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()
