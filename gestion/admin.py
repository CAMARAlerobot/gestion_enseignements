from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Salle, MaterielPedagogique, Classe, Enseignant, Cours

admin.site.register(Salle)
admin.site.register(MaterielPedagogique)
admin.site.register(Classe)
admin.site.register(Enseignant)
admin.site.register(Cours)
