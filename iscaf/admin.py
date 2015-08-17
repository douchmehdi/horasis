from django.contrib import admin
from iscaf.models import Eleve, Cursus, Periode, UE, Matiere, Professeur, Enseigne, Chauffeur, Trajet, Surveillant, Surveille, Note

class EleveAdmin(admin.ModelAdmin):
   list_display   = ('nom', 'prenom', 'dateDeNaissance', 'adresse', 'telephone', 'dateInscription')
   list_filter    = ('nom','prenom',)
   date_hierarchy = 'date'
   ordering       = ('date', )
   search_fields  = ('nom', 'prenom')

admin.site.register(Eleve)
admin.site.register(Cursus)
admin.site.register(Periode)
admin.site.register(UE)
admin.site.register(Matiere)
admin.site.register(Professeur)
admin.site.register(Enseigne)
admin.site.register(Chauffeur)
admin.site.register(Trajet)
admin.site.register(Surveillant)
admin.site.register(Surveille)
admin.site.register(Note)
