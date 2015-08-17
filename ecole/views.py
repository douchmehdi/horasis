#-*- coding: utf-8 -*-
from django.shortcuts import render
from ecole.models import Eleve, Professeur, Enseigne, Matiere, AnneeScolaire, Examen, Cursus, Periode, UE
from django.views.generic import ListView, DetailView, CreateView
from django.core.urlresolvers import reverse_lazy
from ecole.forms import EleveForm, ProfesseurForm, ConnexionForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required
def home(request):
	"""page d'acceuil avec les 5 onglets de redirection"""
	return render(request,'ecole/accueil.html',locals())

class ListeEtudiants(ListView):
	model = Eleve
	context_object_name = "Eleve_liste"
	template_name = "ecole/Etudiants.html"

	def get_queryset(self):
		return Eleve.objects.all().order_by("nom")

class DetailEtudiant(DetailView):
	model = Eleve
	context_object_name = "etudiant"
	template_name = "ecole/Etudiant_Detail.html"

class ListeProfesseurs(ListView):
	model = Professeur
	context_object_name = "Professeur_liste"
	template_name = "ecole/Professeurs.html"

class DetailProfesseur(DetailView):
	model = Professeur
	context_object_name = "professeur"
	template_name = "ecole/Professeur_Detail.html"

	def get_context_data(self,**kwargs):
		context=super(DetailProfesseur, self).get_context_data(**kwargs)
		#ajout de la liste des matières
		#on récupère d'abord la liste des id des matières
		matieresid=Enseigne.objects.filter(professeur=self.kwargs['pk']).values_list("matiere",flat=True).distinct()
		#puis on récupère ensuite le nom et le cursus associé à chaque id
		matieres=list()
		for matiere in matieresid:
			matieres.append([Matiere.objects.get(pk=matiere).nom,Matiere.objects.get(pk=matiere).ue.periode.cursus.nom,matiere])
		context['matieres']=matieres
		return context

class EleveCreate(CreateView):
    model = Eleve
    template_name ='ecole/eleve_nouveau.html'
    form_class = EleveForm
    success_url = 'Etudiants'

def HistoriqueCours(request, id_p,id_m):
	"""Pour une matière enseignée par un professeur, la page affiche les dates auxquelle il les a dispensé"""
	historique=Enseigne.objects.filter(Q(matiere=id_m) & Q(professeur=id_p)).values_list("date",flat=True)
	return render(request, 'ecole/historique_cours.html',locals())

class ProfesseurCreate(CreateView):
	model= Professeur
	template_name='ecole/professeur_nouveau.html'
	form_class=ProfesseurForm
	success_url = "Professeurs"
	
class ListeAnneeScolaires(ListView):
	model = AnneeScolaire
	context_object_name = "AnneeScolaires_liste"
	template_name = "ecole/Examens.html"

def Examen_Detail(request, annee_debut, annee_fin):
	"""Liste des examens pour l'année en cours"""
	anneeScolaire=AnneeScolaire.objects.get(anneeDeDebut=annee_debut)
	examens=Examen.objects.filter(Q(anneeScolaire=anneeScolaire) & Q(isDone=True))
	cursus=Cursus.objects.all()
	periodes=Periode.objects.all()
	ues=UE.objects.all()
	matieres=Matiere.objects.all()
	return render(request, 'ecole/examen_cursus.html',locals())




		
