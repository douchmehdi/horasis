#-*- coding: utf-8 -*-
from django.contrib import admin
from ecole.models import AnneeScolaire, Eleve, Cursus, Periode, UE, Matiere, Professeur, Enseigne, Chauffeur, Trajet, Surveillant, Surveille, Note, InscriptionCursus, Session, Examen

class EleveAdmin(admin.ModelAdmin):
   list_display   = ('nom', 'prenom', 'dateDeNaissance', 'adresse', 'telephone', 'dateInscription')
   list_filter    = ('nom','prenom',)
   ordering       = ('nom', )
   search_fields  = ('nom', 'prenom')

class PeriodeAdmin(admin.ModelAdmin):
   list_display   = ('cursus', 'periode',)
   list_filter    = ('cursus','periode',)
   ordering       = ('cursus','periode', )
   search_fields  = ('cursus',)   

class MatiereAdmin(admin.ModelAdmin):
   list_display   = ('ue', 'nom',)
   list_filter    = ('ue','nom',)
   ordering       = ('ue','nom', )
   search_fields  = ('ue',)   

class ProfesseurAdmin(admin.ModelAdmin):
   list_display   = ('nom', 'prenom',)
   list_filter    = ('nom','prenom',)
   ordering       = ('nom','prenom', )
   search_fields  = ('nom',)   

class EnseigneAdmin(admin.ModelAdmin):
   list_display   = ('professeur','matiere','tarifHoraire','date',)
   list_filter    = ('professeur','matiere',)
   ordering       = ('professeur','matiere',)
   search_fields  = ('professeur','matiere',)  

class NoteAdmin(admin.ModelAdmin):
   list_display   = ('note','eleve',)

class SessionAdmin(admin.ModelAdmin):
   list_display   = ('nom',)

class ExamenAdmin(admin.ModelAdmin):
   list_display   = ('matiere','anneeScolaire','session','isDone')

admin.site.register(InscriptionCursus)
admin.site.register(AnneeScolaire)
admin.site.register(Eleve,EleveAdmin)
admin.site.register(Cursus)
admin.site.register(Periode, PeriodeAdmin)
admin.site.register(UE)
admin.site.register(Matiere, MatiereAdmin)
admin.site.register(Professeur, ProfesseurAdmin)
admin.site.register(Enseigne, EnseigneAdmin)
admin.site.register(Chauffeur)
admin.site.register(Trajet)
admin.site.register(Surveillant)
admin.site.register(Surveille)
admin.site.register(Note,NoteAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(Examen, ExamenAdmin)
