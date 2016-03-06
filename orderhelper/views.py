from django.shortcuts import render, get_object_or_404, redirect
from .models import Comanda, Subcomanda, Proiect, Furnizor, Producator, Reper, Status
from .forms import PersoanaForm, ProiectForm, FurnizorForm, ProducatorForm, ReperForm, ComandaForm, ComandaEditForm, SubcomandaForm, SubcomandaEditForm, SubcomandaCloseForm, ComandaCloseForm, SubcomandaCancelForm, ComandaCancelForm
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
	subcomenzi = Subcomanda.objects.all().filter(comanda_ref__pk=pk)
	comanda = Comanda.objects.get(pk=pk)

	return render(request,'orderhelper/comanda_subcomenzi.html', {'subcomenzi':subcomenzi, 'comanda':comanda})

@login_required
def dashboard(request):
	return render(request,'orderhelper/dashboard.html', {})

@login_required
def order_history(request):
	groups_list = request.user.groups.all()
	comenda_list = Comanda.objects.all().filter(status__text='Inchis',group__in=groups_list).order_by('data')
	paginator = Paginator(comenda_list, 5)
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

	return render(request,'orderhelper/proiect_all.html', {'proiecte':proiecte})

@login_required
def furnizor_all(request):
	groups_list = request.user.groups.all()
	furnizori = Furnizor.objects.all().filter(group__in=groups_list).order_by('pk')

	return render(request,'orderhelper/furnizor_all.html', {'furnizori':furnizori})


@login_required
def producator_all(request):
	groups_list = request.user.groups.all()
	producatori = Producator.objects.all().filter(group__in=groups_list).order_by('pk')

	return render(request,'orderhelper/producator_all.html', {'producatori':producatori})

@login_required
def reper_all(request):
	groups_list = request.user.groups.all()
	reperi = Reper.objects.all().filter(group__in=groups_list).order_by('pk')

	return render(request,'orderhelper/reper_all.html', {'reperi':reperi})

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
	subcomenzi = Subcomanda.objects.all().filter(group__in=groups_list,data__gte=datetime.now()-timedelta(days=30)).order_by('pk')

	return render(request,'orderhelper/subcomanda_all.html', {'subcomenzi':subcomenzi})

@login_required
def comanda_new(request):
	status_deschis = Status.objects.all().filter(text='Deschis')[0]

	if request.method == "POST":
		comandaform = ComandaForm(request.POST)
		if comandaform.is_valid():
			comanda = comandaform.save(commit=False)
			comanda.status = status_deschis
			comanda.data = datetime.now()
			comanda.preluat = request.user
			comanda.save()
			comandaform.save_m2m()
			return redirect('comanda_all')

	comandaform = ComandaForm()
	return render(request,'orderhelper/comanda_new.html', {'comandaform':comandaform})


@login_required
def subcomanda_new(request):
	status_deschis = Status.objects.all().filter(text='Deschis')[0]

	if request.method == "POST":
		subcomandaform = SubcomandaForm(request.POST)
		if subcomandaform.is_valid():
			subcomanda = subcomandaform.save(commit=False)
			subcomanda.status = status_deschis
			numar_curent = 0
			if Subcomanda.objects.all().filter(comanda_ref__numar_unic=subcomanda.comanda_ref.numar_unic).exists(): 
				numar_curent = Subcomanda.objects.all().filter(comanda_ref__numar_unic=subcomanda.comanda_ref.numar_unic).latest('pk').numar_curent

			subcomanda.numar_curent = numar_curent + 1
			subcomanda.data = datetime.now()
			subcomanda.save()
			subcomandaform.save_m2m()
			return redirect('subcomanda_all')
		
	subcomandaform = SubcomandaForm()
	return render(request,'orderhelper/subcomanda_new.html', {'subcomandaform':subcomandaform})

@login_required
def subcomanda_edit(request,pk):
	subcomanda = get_object_or_404(Subcomanda, pk=pk)
	if request.method == "POST":
		subcomandaform = SubcomandaEditForm(request.POST, instance=subcomanda)
		if subcomandaform.is_valid():
			subcomanda = subcomandaform.save(commit=False)
			subcomanda.save()		
			return redirect('subcomanda_all')
		
	subcomandaform = SubcomandaEditForm(instance=subcomanda)	
	return render(request,'orderhelper/subcomanda_edit.html', {'subcomandaform' : subcomandaform})

@login_required
def comanda_edit(request, pk):
	comanda = get_object_or_404(Comanda, pk=pk)
	
	if request.method == "POST":
		comandaform = ComandaEditForm(request.POST, instance=comanda)
		if comandaform.is_valid():
			comanda = comandaform.save(commit=True)
			comanda.save()
			return redirect('comanda_all')
			

	comandaform = ComandaEditForm(instance=comanda)
	return render(request,'orderhelper/comanda_edit.html', {'comandaform':comandaform})


@login_required
def reper_new(request):

	if request.method == "POST":
		form = ReperForm(request.POST)
		if form.is_valid():
			reper = form.save(commit=True)
			reper.save()
			return redirect(request.META['HTTP_REFERER'])
	
	form = ReperForm()
	return render(request,'orderhelper/reper_new.html', {'form': form})

@login_required
def producator_new(request):

	if request.method == "POST":
		form = ProducatorForm(request.POST)
		if form.is_valid():
			producator = form.save(commit=True)
			producator.save()
			return redirect(request.META['HTTP_REFERER'])

	form = ProducatorForm()
	return render(request,'orderhelper/producator_new.html', {'form': form})

@login_required
def furnizor_new(request):

	if request.method == "POST":
		form = FurnizorForm(request.POST)
		if form.is_valid():
			furnizor = form.save(commit=True)
			furnizor.save()
			return redirect(request.META['HTTP_REFERER'])
	
	form = FurnizorForm()
	return render(request,'orderhelper/furnizor_new.html', {'form': form})

@login_required
def proiect_new(request):

	if request.method == "POST":
		form = ProiectForm(request.POST)
		if form.is_valid():
			proiect = form.save(commit=True)
			proiect.save()
			return redirect(request.META['HTTP_REFERER'])
	
	form = ProiectForm()
	return render(request,'orderhelper/proiect_new.html', {'form': form})

@login_required
def persoana_new(request):
	
	if request.method == "POST":
		form = PersoanaForm(request.POST)
		if form.is_valid():
			persoana = form.save(commit=True)
			persoana.save()
			return redirect(request.META['HTTP_REFERER'])
	
	form = PersoanaForm()
	return render(request,'orderhelper/persoana_new.html', {'form': form})

@login_required
def producator_edit(request, pk):
	producator = get_object_or_404(Producator, pk=pk)
	if request.method == "POST":
		form = ProducatorForm(request.POST,instance=producator)
		if form.is_valid():
			producator = form.save(commit=True)
			producator.save()
			return redirect(request.META['HTTP_REFERER'])

	form = ProducatorForm(instance=producator)
	return render(request,'orderhelper/producator_edit.html', {'form': form})

@login_required
def pending_subcomanda_close(request, pk):
	subcomanda = get_object_or_404(Subcomanda, pk=pk)
	status_inchis = Status.objects.filter(text='Inchis')[0]
	dialog_title = "Inchide subcomanda"
	url = '/subcomanda/close/' + pk
	if request.method == "POST":
		form = SubcomandaCloseForm(request.POST,instance=subcomanda)
		if form.is_valid():
			subcomanda = form.save(commit=False)
			subcomanda.status = status_inchis
			subcomanda.save()
			return redirect(request.META['HTTP_REFERER'])

	form = SubcomandaCloseForm(instance=subcomanda)
	return render(request,'orderhelper/pending_modal_edit.html', {'form': form, 'subcomanda':subcomanda, 'dialog_title':dialog_title, 'url':url})

@login_required
def pending_comanda_close(request, pk):
	comanda = get_object_or_404(Comanda, pk=pk)
	status_inchis = Status.objects.filter(text='Inchis')[0]
	dialog_title = "Inchide comanda"
	url = '/comanda/close/' + pk

	if request.method == "POST":
		form = ComandaCloseForm(request.POST,instance=comanda)
		if form.is_valid():
			comanda = form.save(commit=False)
			comanda.status = status_inchis
			comanda.save()
			return redirect(request.META['HTTP_REFERER'])

	form = ComandaCloseForm(instance=comanda)
	return render(request,'orderhelper/pending_modal_edit.html', {'form': form, 'comanda':comanda, 'dialog_title':dialog_title, 'url': url})

@login_required
def pending_subcomanda_cancel(request, pk):
	subcomanda = get_object_or_404(Subcomanda, pk=pk)
	status_anulat = Status.objects.filter(text='Anulat')[0]
	dialog_title = "Anuleaza subcomanda"
	url = '/subcomanda/cancel/' + pk

	if request.method == "POST":
		form = SubcomandaCancelForm(request.POST,instance=subcomanda)
		if form.is_valid():
			subcomanda = form.save(commit=False)
			subcomanda.status = status_anulat
			subcomanda.save()
			return redirect(request.META['HTTP_REFERER'])

	form = SubcomandaCancelForm(instance=subcomanda)
	return render(request,'orderhelper/pending_subcomanda_cancel.html', {'form': form, 'subcomanda':subcomanda, 'dialog_title':dialog_title, 'url':url})

@login_required
def pending_comanda_cancel(request, pk):
	comanda = get_object_or_404(Comanda, pk=pk)
	status_anulat = Status.objects.filter(text='Anulat')[0]
	dialog_title = "Anuleaza comanda"
	url = '/comanda/cancel/' + pk

	if request.method == "POST":
		form = ComandaCancelForm(request.POST,instance=comanda)
		if form.is_valid():
			comanda = form.save(commit=False)
			comanda.status = status_anulat
			comanda.save()
			subcomenzi = Subcomanda.objects.all().filter(comanda_ref__pk=pk)
			for subcomanda in subcomenzi:
				subcomanda.status = status_anulat
				subcomanda.save()
			return redirect(request.META['HTTP_REFERER'])

	form = ComandaCancelForm(instance=comanda)
	return render(request,'orderhelper/pending_comanda_cancel.html', {'form': form, 'comanda':comanda, 'dialog_title':dialog_title, 'url':url})


