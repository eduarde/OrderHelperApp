from django.db import models
from django.utils import timezone
from django.utils.timezone import now
from datetime import date, timedelta
from django.contrib.auth.models import Group

class Valuta(models.Model):
	DOLLARS = 'USD'
	EURO = 'EURO'
	RON = 'RON'

	VALUTA_CHOICES = (
		(DOLLARS, 'USD'),
		(EURO, 'EURO'),
		(RON, 'RON'),
	)
	text = models.CharField(max_length=5, choices=VALUTA_CHOICES, default=RON)

	def __str__(self):
		return self.text 

class Status(models.Model):
	DESCHIS = 'Deschis'
	INCHIS = 'Inchis'
	ANULAT = 'Anulat'

	STATUS_CHOICES = (
		(DESCHIS, 'Deschis'),
		(INCHIS, 'Inchis'),
		(ANULAT, 'Anulat'),
	)

	text = models.CharField(max_length=20, choices=STATUS_CHOICES, default=DESCHIS)

	def __str__(self):
		return self.text

class Persoana(models.Model):
	nume = models.CharField('Nume', max_length=100)
	prenume = models.CharField('Prenume', max_length=100)
	telefon = models.CharField('Telefon', max_length=10, blank=True, null=True)
	group = models.ManyToManyField(Group, related_name='persoanas')

	def __str__(self):
		return self.nume + ' ' + self.prenume;

class Proiect(models.Model):
	titlu = models.CharField('Denumire', blank=False, null=False, max_length=255)
	descriere = models.TextField('Descriere', blank=True, null=True)
	group = models.ManyToManyField(Group,blank=False, null=False, related_name='proiects')

	def __str__(self):
		return self.titlu

class Producator(models.Model):
	nume = models.CharField('Nume', max_length=255)
	descriere = models.TextField('Descriere', blank=True, null=True)
	telefon = models.CharField('Telefon', max_length=10, blank=True, null=True)
	group = models.ManyToManyField(Group, related_name='producators')

	def __str__(self):
		return self.nume

class Furnizor(models.Model):
	nume = models.CharField('Nume', max_length=255)
	descriere = models.TextField('Descriere', blank=True, null=True)
	telefon = models.CharField('Telefon', max_length=10, blank=True, null=True)
	group = models.ManyToManyField(Group, related_name='furnizors')

	def __str__(self):
		return self.nume

class TermenPlata(models.Model):
	tip = models.CharField('Tip termen', max_length=50)

	def __str__(self):
		return self.tip

class ModPlata(models.Model):
	tip = models.CharField('Mod plata', max_length=50)

	def __str__(self):
		return self.tip

class Reper(models.Model):
	cod_reper = models.CharField('Cod reper', max_length=100, null=True)
	reper = models.TextField('Reper',null=True)
	link = models.URLField('Link',blank=True,null=True)
	group = models.ManyToManyField(Group, related_name='repers')

	def __str__(self):
		return self.cod_reper

class Subcomanda(models.Model):
	comanda_ref = models.ForeignKey('Comanda', null=True, verbose_name='Comanda') 
	numar_curent = models.IntegerField('Numar Curent',null=True)
	status = models.ForeignKey('Status',null=True)
	producator = models.ForeignKey('Producator',blank=True, null=True)
	reper = models.ForeignKey('Reper', null=True)
	furnizor = models.ForeignKey('Furnizor', null=True)
	cantitate = models.DecimalField('Cantitate', default=0, max_digits=9, decimal_places=0, null=True)
	data_livrare = models.DateField('Data livrare',null=True)
	data_primire = models.DateField('Data primire',blank=False, null=True)
	pret = models.DecimalField('Pret', default=0, max_digits=9, decimal_places=2, null=True)
	valuta = models.ForeignKey('Valuta', null=True, verbose_name='Valuta')
	data = models.DateField('Data',default=now())

	def set_pret_total(self):
		return self.pret * self.cantitate

	pret_total = property(set_pret_total)
	termen_plata = models.ForeignKey('TermenPlata', null=True)
	mod_plata = models.ForeignKey('ModPlata', null=True)
	group = models.ManyToManyField(Group, related_name='subcomandas')

	def is_late(self):
		if self.status.text != 'Deschis':
			return False
		return date.today().isoformat() > self.data_livrare.isoformat()

	def is_today(self):
		if self.status.text != 'Deschis':
			return False
		return date.today().isoformat() == self.data_livrare.isoformat()	

	def __str__(self):
		return 'Subcomanda: ' + str(self.numar_curent)


class Comanda(models.Model):
	status = models.ForeignKey('Status', null=True)
	data = models.DateField('Data',default=now())
	obiect_succint = models.TextField('Obiect Succint', null=True)
	solicitant = models.ForeignKey('Persoana',null=True, verbose_name='Solicitant')
	# cc = models.ForeignKey('Persoana', null=True, blank=True, verbose_name='CC')
	preluat = models.ForeignKey('auth.User', verbose_name='Preluare', null=True)
	proiect = models.ForeignKey('Proiect', null=True)

	def set_pret_total(self):
		subcomenzi = Subcomanda.objects.exclude(status__text='Anulat').filter(comanda_ref__pk=self.pk)
		total = 0
		for subcomanda in subcomenzi:
			total += subcomanda.pret_total
		return total

	pret_total = property(set_pret_total)
	data_primire = models.DateField('Data primire',blank=False, null=True)
	group = models.ManyToManyField(Group, related_name='coamandas')


	def is_late(self):
		subcomenzi = Subcomanda.objects.all().filter(comanda_ref__pk=self.pk, status__text='Deschis')
		for subcomanda in subcomenzi:
			if date.today().isoformat() > subcomanda.data_livrare.isoformat():
				return True
		return False

	def is_today(self):
		subcomenzi = Subcomanda.objects.all().filter(comanda_ref__pk=self.pk, status__text='Deschis')
		for subcomanda in subcomenzi:
			if date.today().isoformat() == subcomanda.data_livrare.isoformat():
				return True
		return False

	def calculate_progress(self):
		subcomenzi_total = Subcomanda.objects.exclude(status__text='Anulat').filter(comanda_ref__pk=self.pk).count()
		subcomenzi_finished = Subcomanda.objects.all().filter(comanda_ref__pk=self.pk,status__text='Inchis').count()
		if subcomenzi_total == 0:
			return 0
		return ( subcomenzi_finished * 100 ) / subcomenzi_total

	def show_subcomenzi(self):
		return Subcomanda.objects.all().filter(comanda_ref__pk=self.pk)

	def show_valuta(self):
		return	Subcomanda.objects.filter(comanda_ref__pk=self.pk).latest('pk').valuta
		
	def __str__(self):
		return 'Comanda: ' + str(self.pk)
