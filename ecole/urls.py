#-*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic import ListView
from ecole.views import ListeEtudiants, DetailEtudiant, ListeProfesseurs, DetailProfesseur, EleveCreate, ProfesseurCreate, ListeAnneeScolaires
#from django.contrib.auth.views import login


urlpatterns = patterns('ecole.views',
	url(r'^accueil$', 'home'),
	url(r'^Etudiants$',ListeEtudiants.as_view(),name="Etudiants"),
	url(r'^Etudiant_Detail/(?P<pk>\d+)$', DetailEtudiant.as_view(), name="Etudiant_Detail"),
	url(r'^Professeurs$',ListeProfesseurs.as_view(),name="Professeurs"),
	url(r'^Professeur_Detail/(?P<pk>\d+)$', DetailProfesseur.as_view(), name="Professeur_Detail"),
	url(r'^eleve_nouveau$', EleveCreate.as_view(), name='eleve_nouveau'),
	#url(r'^connexion$', 'django.contrib.auth.views.login', {'template_name': 'ecole/connexion.html'})
	url(r'^HistoriqueCours/(?P<id_p>\d+)/(?P<id_m>\d+)$','HistoriqueCours'),
	url(r'^professeur_nouveau$', ProfesseurCreate.as_view(), name='professeur_nouveau'),
	url(r'^Examens$',ListeAnneeScolaires.as_view(),name="Examens"),
	url(r'^examen/(?P<annee_debut>\d+)/(?P<annee_fin>\d+)$','Examen_Detail',name="Examens"),


)