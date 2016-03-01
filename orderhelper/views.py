from django.shortcuts import render, get_object_or_404, redirect
from .models import Comanda, Subcomanda, Proiect, Furnizor, Producator, Reper, Status
from .forms import PersoanaForm, ProiectForm, FurnizorForm, ProducatorForm, ReperForm, ComandaForm, SubcomandaForm
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from datetime import date, datetime, timedelta

@login_required
def pending_comanda(request):
	groups_list = request.user.groups.all()
	comenzi = Comanda.objects.all().filter(status__text='Deschis',group__in=groups_list).order_by('data')
	return render(request,'orderhelper/pending_comanda.html', {'comenzi':comenzi})

@login_required
def comanda_subcomenzi(request, pk):
	comanda = get_object_or_404(Comanda, pk=pk)
	# subcomenzi = Subcomanda.objects.all().filter(comanda_ref__numar_unic=476)
	subcomenzi = Subcomanda.objects.all().filter(comanda_ref__pk=pk)
	comanda = Comanda.objects.get(pk=pk)
	return render(request,'orderhelper/comanda_subcomenzi.html', {'subcomenzi':subcomenzi, 'comanda':comanda})

@login_required
def persoana_new(request):
	form = PersoanaForm()
	return render(request,'orderhelper/persoana_new.html', {'form': form})

@login_required
def dashboard(request):
	return render(request,'orderhelper/dashboard.html', {})

@login_required
def order_history(request):
	groups_list = request.user.groups.all()
	comenda_list = Comanda.objects.all().filter(status__text='Inchis',group__in=groups_list).order_by('data')
	paginator = Paginator(comenda_list, 1)
	page = request.GET.get('page')
	try:
		comenzi = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		comenzi = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		comenzi = paginator.page(paginator.num_pages)
	return render(request,'orderhelper/order_history.html', {'comenzi' : comenzi})

@login_required
def proiect_all(request):
	groups_list = request.user.groups.all()
	proiecte = Proiect.objects.all().filter(group__in=groups_list).order_by('pk')

	if request.method == "POST":
		form = ProiectForm(request.POST)
		if form.is_valid():
			proiect = form.save(commit=True)
			proiect.save()
			return redirect('proiect_all')
	else:
		form = ProiectForm()

	return render(request,'orderhelper/proiect_all.html', {'proiecte':proiecte, 'form': form})

@login_required
def furnizor_all(request):
	groups_list = request.user.groups.all()
	furnizori = Furnizor.objects.all().filter(group__in=groups_list).order_by('pk')

	if request.method == "POST":
		form = FurnizorForm(request.POST)
		if form.is_valid():
			furnizor = form.save(commit=True)
			furnizor.save()
			return redirect('furnizor_all')
	else:
		form = FurnizorForm()

	return render(request,'orderhelper/furnizor_all.html', {'furnizori':furnizori, 'form': form})


@login_required
def producator_all(request):
	groups_list = request.user.groups.all()
	producatori = Producator.objects.all().filter(group__in=groups_list).order_by('pk')

	if request.method == "POST":
		form = ProducatorForm(request.POST)
		if form.is_valid():
			producator = form.save(commit=True)
			producator.save()
			return redirect('producator_all')
	else:
		form = ProducatorForm()

	return render(request,'orderhelper/producator_all.html', {'producatori':producatori, 'form': form})

@login_required
def reper_all(request):
	groups_list = request.user.groups.all()
	reperi = Reper.objects.all().filter(group__in=groups_list).order_by('pk')

	if request.method == "POST":
		form = ReperForm(request.POST)
		if form.is_valid():
			reper = form.save(commit=True)
			reper.save()
			return redirect('reper_all')
	else:
		form = ReperForm()

	return render(request,'orderhelper/reper_all.html', {'reperi':reperi, 'form': form})

@login_required
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def comanda_all(request):
	groups_list = request.user.groups.all()
	comenzi = Comanda.objects.all().filter(group__in=groups_list,data__gte=datetime.now()-timedelta(days=30)).order_by('pk')
	return render(request,'orderhelper/comanda_all.html', {'comenzi':comenzi})

@login_required
def subcomanda_all(request):
	groups_list = request.user.groups.all()
	subcomenzi = Subcomanda.objects.all().filter(group__in=groups_list).order_by('pk')
	# subcomenzi = Subcomanda.objects.all().filter(group__in=groups_list,data_livrare__gte=datetime.now()-timedelta(days=30)).order_by('pk')
	return render(request,'orderhelper/subcomanda_all.html', {'subcomenzi':subcomenzi})

@login_required
def comanda_new(request):
	status_deschis = Status.objects.all().filter(text='Deschis')[0]

	if request.method == "POST":
		if 'newcomanda' in request.POST:
			comandaform = ComandaForm(request.POST)
			if comandaform.is_valid():
				comanda = comandaform.save(commit=False)
				comanda.status = status_deschis
				comanda.data = datetime.now()
				comanda.preluat = request.user
				comanda.save()
				comandaform.save_m2m()
				return redirect('comanda_all')
			proiectform = ProiectForm()
			solicitantform = PersoanaForm()
		elif 'newproiect' in request.POST:
			proiectform = ProiectForm(request.POST)
			if proiectform.is_valid():
				proiect = proiectform.save(commit=True)
				proiect.save()
			comandaform = ComandaForm()
			solicitantform = PersoanaForm()
		elif 'newsolicitant' in request.POST:
			solicitantform = PersoanaForm(request.POST)
			if solicitantform.is_valid():
				solicitant = solicitantform.save(commit=True)
				solicitant.save()
			comandaform = ComandaForm()
			proiectform = ProiectForm()

	else:
		comandaform = ComandaForm()
		proiectform = ProiectForm()
		solicitantform = PersoanaForm()

	return render(request,'orderhelper/comanda_new.html', {'comandaform':comandaform, 'proiectform':proiectform, 'solicitantform':solicitantform})


@login_required
def subcomanda_new(request):
	status_deschis = Status.objects.all().filter(text='Deschis')[0]


	if request.method == "POST":
		if 'newsubcomanda' in request.POST:
			subcomandaform = SubcomandaForm(request.POST)
			if subcomandaform.is_valid():
				subcomanda = subcomandaform.save(commit=False)
				subcomanda.status = status_deschis
				last_subcomanda = Subcomanda.objects.all().filter(comanda_ref__numar_unic=subcomanda.comanda_ref.numar_unic).latest('pk')
				subcomanda.numar_curent = last_subcomanda.numar_curent + 1
				subcomanda.save()
				subcomandaform.save_m2m()
				return redirect('subcomanda_all')
		elif 'newproducator' in request.POST:
			producatorform = ProducatorForm(request.POST)
			if producatorform.is_valid():
				producator = producatorform.save(commit=True)
				producator.save()
			subcomandaform = SubcomandaForm()
			furnizorform = FurnizorForm()
			reperform = ReperForm()
		elif 'newfurnizor' in request.POST:
			furnizorform = FurnizorForm(request.POST)
			if furnizorform.is_valid():
				furnizor = furnizorform.save(commit=True)
				furnizor.save()
			subcomandaform = SubcomandaForm()
			producatorform = ProducatorForm()
			reperform = ReperForm()
		elif 'newreper' in request.POST:
			reperform = ReperForm(request.POST)
			if reperform.is_valid():
				reper = reperform.save(commit=True)
				reper.save()
			subcomandaform = SubcomandaForm()
			producatorform = ProducatorForm()
			furnizorform = FurnizorForm()
	else:
		subcomandaform = SubcomandaForm()
		producatorform = ProducatorForm()
		furnizorform = FurnizorForm()
		reperform = ReperForm()

	return render(request,'orderhelper/subcomanda_new.html', {'subcomandaform':subcomandaform, 'producatorform':producatorform, 'furnizorform':furnizorform, 'reperform':reperform})