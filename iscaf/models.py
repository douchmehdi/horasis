#-*- coding: utf-8 -*-
from django.db import models
from django.core.validators import RegexValidator

class Eleve(models.Model):
	nom=models.CharField(max_length=40)
	prenom=models.CharField(max_length=40)
	dateDeNaissance=models.DateTimeField(verbose_name="date de naissance")
	adresse=models.CharField(max_length=300)
	telephone=RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	dateInscription=models.DateTimeField(verbose_name="date d'inscription")

	def __unicode__(self):
		return "Nom : {0}, Prenom : {1}".format(self.nom,self.prenom)

class Cursus(models.Model):
	nom=models.CharField(max_length=40)

	def __unicode__(self):
		return self.nom

class Periode(models.Model):
	periode=models.IntegerField(max_length=2,default=0)
	cursus=models.ForeignKey('Cursus')
	def __unicode__(self):
		return self.periode

class UE(models.Model):
	nom=models.CharField(max_length=40)
	nombreMatieres=models.IntegerField(max_length=10,default=8)
	periode=models.ForeignKey(Periode)

	def __unicode__(self):
		return "L'UE {0} est composée de {1} matières".format(self.nom,self.nombreMatieres)

class Matiere(models.Model):
	"""Ensembe de toutes les matières enseingnées à l'iscaf"""
	nom=models.CharField(max_length=200)
	ue=models.ForeignKey(UE)

	def __unicode__(self):
		return self.nom

class Professeur(models.Model):
	"""Professeurs assurant les cours à l'ISCAF"""
	nom=models.CharField(max_length=40)
	prenom=models.CharField(max_length=40)
	matieres=models.ManyToManyField(Matiere, through='Enseigne')

	def __unicode__(self):
		return self.nom

class Enseigne(models.Model):
	"""table intermédiaire permettant de relier les professeurs aux cours qu'ils ont donné"""
	date=models.DateTimeField(verbose_name="Cours dispensés")
	tarifHoraire=models.DecimalField(max_digits=5, decimal_places=2, verbose_name="tarif horaire en euros")
	professeur=models.ForeignKey(Professeur)
	matiere=models.ForeignKey(Matiere)

	def __unicode__(self):
		return "{0} à enseigné {1} le {2}".format(self.professeur.nom,self.matiere.nom,self.date)

class Chauffeur(models.Model):
	"""Chauffeurs emmenant et ramnenant les professeurs à l'ISCAF"""
	nom=models.CharField(max_length=40)
	prenom=models.CharField(max_length=40)

	def __unicode__(self):
		return self.prenom

class Trajet(models.Model):
	"""Trajets entre l'ISCAF et l'aéroport"""
	date=models.DateTimeField(verbose_name="date du trajet")
	sens=models.DateTimeField(verbose_name="Sens AI ou IA")
	chauffeur=models.ForeignKey(Chauffeur)
	Professeur=models.ForeignKey(Professeur)

	def __unicode__(self):
		return "{0} à conduit {1} dans le sens {2} le {3}".format(self.chauffeur.nom,self.professeur.nom,self.sens,self.date)

class Surveillant(models.Model):
	"""Surveillants de l'ISCAF"""
	nom=models.CharField(max_length=40)
	prenom=models.CharField(max_length=40)
	matiere=models.ManyToManyField(Matiere, through='Surveille')

	def __unicode__(self):
		return self.nom

class Surveille(models.Model):
	"""Surveillances effectuées par les surveillants"""
	date=models.DateTimeField(verbose_name="date de l'examen")
	duree=models.DecimalField(max_digits=5, decimal_places=1, verbose_name="durée de la surveillance")
	surveillant=models.ForeignKey(Surveillant)
	matiere=models.ForeignKey(Matiere)

	def __unicode__(self):
		return "{0} à surveillé {1} le {3}".format(self.surveillant.nom,self.matiere.nom,self.date)

class Note(models.Model):
	"""Notes obtenues par les élèves"""
	note=models.DecimalField(max_digits=5, decimal_places=2)
	eleve=models.ForeignKey(Eleve)
	matiere=models.ForeignKey(Matiere)

	def __unicode__(self):
		return "{0} à obtenu la note de {1} en {3}".format(self.eleve.nom,self.note,self.matiere.nom)