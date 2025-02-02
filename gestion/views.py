from django.shortcuts import render
from .models import Salle, MaterielPedagogique, Classe, Enseignant, Cours

def index(request):
    salles = Salle.objects.all()
    materiels = MaterielPedagogique.objects.all()
    classes = Classe.objects.all()
    enseignants = Enseignant.objects.all()
    cours = Cours.objects.all()
    return render(request, 'gestion/index.html', {
        'salles': salles,
        'materiels': materiels,
        'classes': classes,
        'enseignants': enseignants,
        'cours': cours,
    })

# Create your views here.
