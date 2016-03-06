from django.shortcuts import render, get_object_or_404, redirect
from .models import Comanda, Subcomanda, Proiect, Furnizor, Producator, Reper, Status
from .forms import PersoanaForm, ProiectForm, FurnizorForm, ProducatorForm, ReperForm, ComandaForm, ComandaEditForm, SubcomandaForm, SubcomandaEditForm, SubcomandaCloseForm, ComandaCloseForm, SubcomandaCancelForm, ComandaCancelForm
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from datetime import date, datetime, timedelta
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger


# def handler404(request):
# 	return render(request,'orderhelper/error404.html');

@login_required
def pending(request):
	groups_list = request.user.groups.all()
	comenzi = Comanda.objects.all().filter(status__text='Deschis',group__in=groups_list).order_by('data')

	return render(request,'orderhelper/pending.html', {'comenzi':comenzi})

# @login_required
# def comanda_subcomenzi(request, pk):
# 	comanda = get_object_or_404(Comanda, pk=pk)
# 	subcomenzi = Subcomanda.objects.all().filter(comanda_ref__pk=pk)
# 	comanda = Comanda.objects.get(pk=pk)

# 	return render(request,'orderhelper/comanda_subcomenzi.html', {'subcomenzi':subcomenzi, 'comanda':comanda})

@login_required
def dashboard(request):
	return render(request,'orderhelper/dashboard.html', {})

@login_required
def history(request):
	groups_list = request.user.groups.all()
	comanda_list = Comanda.objects.all().filter(status__text='Inchis',group__in=groups_list).order_by('data')

	try:
		page = request.GET.get('page', 1)
	except PageNotAnInteger:
		page = 1

	p = Paginator(comanda_list, 8)
	comenzi = p.page(page)

	return render(request,'orderhelper/history.html', {'comenzi' : comenzi})

@login_required
def dashboard_proiect(request):
	groups_list = request.user.groups.all()
	proiect_list = Proiect.objects.all().filter(group__in=groups_list).order_by('pk')

	try:
		page = request.GET.get('page', 1)
	except PageNotAnInteger:
		page = 1

	p = Paginator(proiect_list, 8)
	proiecte = p.page(page)

	return render(request,'orderhelper/dashboard_proiect.html', {'proiecte':proiecte})

@login_required
def dashboard_furnizor(request):
	groups_list = request.user.groups.all()
	furnizor_list = Furnizor.objects.all().filter(group__in=groups_list).order_by('pk')

	try:
		page = request.GET.get('page', 1)
	except PageNotAnInteger:
		page = 1

	p = Paginator(furnizor_list, 8)
	furnizori = p.page(page)

	return render(request,'orderhelper/dashboard_furnizor.html', {'furnizori':furnizori})


@login_required
def dashboard_producator(request):
	groups_list = request.user.groups.all()
	producator_list = Producator.objects.all().filter(group__in=groups_list).order_by('pk')

	try:
		page = request.GET.get('page', 1)
	except PageNotAnInteger:
		page = 1

	p = Paginator(producator_list, 8)
	producatori = p.page(page)

	return render(request,'orderhelper/dashboard_producator.html', {'producatori':producatori})

@login_required
def dashboard_reper(request):
	groups_list = request.user.groups.all()
	reper_list = Reper.objects.all().filter(group__in=groups_list).order_by('pk')

	try:
		page = request.GET.get('page', 1)
	except PageNotAnInteger:
		page = 1

	p = Paginator(reper_list, 5)
	reperi = p.page(page)

	return render(request,'orderhelper/dashboard_reper.html', {'reperi':reperi})

@login_required
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def dashboard_comanda(request):
	groups_list = request.user.groups.all()
	comanda_list = Comanda.objects.all().filter(group__in=groups_list,data__gte=datetime.now()-timedelta(days=30)).order_by('-data')

	try:
		page = request.GET.get('page', 1)
	except PageNotAnInteger:
		page = 1

	p = Paginator(comanda_list, 8)
	comenzi = p.page(page)

	return render(request,'orderhelper/dashboard_comanda.html', {'comenzi':comenzi})

@login_required
def dashboard_subcomanda(request):
	groups_list = request.user.groups.all()
	subcomanda_list = Subcomanda.objects.all().filter(group__in=groups_list,data__gte=datetime.now()-timedelta(days=30)).order_by('-data')

	try:
		page = request.GET.get('page', 1)
	except PageNotAnInteger:
		page = 1

	p = Paginator(subcomanda_list, 6)
	subcomenzi = p.page(page)

	return render(request,'orderhelper/dashboard_subcomanda.html', {'subcomenzi':subcomenzi})

@login_required
def dashboard_comanda_new(request):
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
			return redirect('dashboard_comanda')

	comandaform = ComandaForm()
	return render(request,'orderhelper/dashboard_comanda_new.html', {'comandaform':comandaform})

@login_required
def dashboard_comanda_edit(request, pk):
	comanda = get_object_or_404(Comanda, pk=pk)
	
	if request.method == "POST":
		comandaform = ComandaEditForm(request.POST, instance=comanda)
		if comandaform.is_valid():
			comanda = comandaform.save(commit=True)
			comanda.save()
			return redirect('dashboard_comanda')
			
	comandaform = ComandaEditForm(instance=comanda)
	return render(request,'orderhelper/dashboard_comanda_edit.html', {'comandaform':comandaform})


@login_required
def dashboard_subcomanda_new(request):
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
			return redirect('dashboard_subcomanda')
		
	subcomandaform = SubcomandaForm()
	return render(request,'orderhelper/dashboard_subcomanda_new.html', {'subcomandaform':subcomandaform})

@login_required
def dashboard_subcomanda_edit(request,pk):
	subcomanda = get_object_or_404(Subcomanda, pk=pk)
	if request.method == "POST":
		subcomandaform = SubcomandaEditForm(request.POST, instance=subcomanda)
		if subcomandaform.is_valid():
			subcomanda = subcomandaform.save(commit=False)
			subcomanda.save()		
			return redirect('dashboard_subcomanda')
		
	subcomandaform = SubcomandaEditForm(instance=subcomanda)	
	return render(request,'orderhelper/dashboard_subcomanda_edit.html', {'subcomandaform' : subcomandaform})




@login_required
def reper_new(request):
	dialog_title = 'Adauga reper'
	url = '/reper/new/'

	if request.method == "POST":
		form = ReperForm(request.POST)
		if form.is_valid():
			reper = form.save(commit=True)
			reper.save()
			return redirect(request.META['HTTP_REFERER'])
	
	form = ReperForm()
	return render(request,'orderhelper/modal_dialog.html', {'form': form, 'dialog_title':dialog_title, 'url': url})

@login_required
def reper_edit(request, pk):
	reper = get_object_or_404(Reper, pk=pk)
	dialog_title = "Editeaza reper"
	url = '/reper/edit/' + pk

	if request.method == "POST":
		form = ReperForm(request.POST,instance=reper)
		if form.is_valid():
			reper = form.save(commit=True)
			reper.save()
			return redirect(request.META['HTTP_REFERER'])
	
	form = ReperForm(instance=reper)
	return render(request,'orderhelper/modal_dialog.html', {'form': form, 'dialog_title':dialog_title, 'url':url})

@login_required
def producator_new(request):
	dialog_title = "Adauga producator"
	url = '/producator/new/'

	if request.method == "POST":
		form = ProducatorForm(request.POST)
		if form.is_valid():
			producator = form.save(commit=True)
			producator.save()
			return redirect(request.META['HTTP_REFERER'])

	form = ProducatorForm()
	return render(request,'orderhelper/modal_dialog.html', {'form': form, 'dialog_title':dialog_title, 'url':url})

@login_required
def furnizor_new(request):
	dialog_title = "Adauga furnizor"
	url = '/furnizor/new/'

	if request.method == "POST":
		form = FurnizorForm(request.POST)
		if form.is_valid():
			furnizor = form.save(commit=True)
			furnizor.save()
			return redirect(request.META['HTTP_REFERER'])
	
	form = FurnizorForm()
	return render(request,'orderhelper/modal_dialog.html', {'form': form, 'dialog_title':dialog_title, 'url': url})

@login_required
def furnizor_edit(request,pk):
	furnizor = get_object_or_404(Furnizor, pk=pk)
	dialog_title = "Editeaza furnizor"
	url = '/furnizor/new/'

	if request.method == "POST":
		form = FurnizorForm(request.POST, instance=furnizor)
		if form.is_valid():
			furnizor = form.save(commit=True)
			furnizor.save()
			return redirect(request.META['HTTP_REFERER'])
	
	form = FurnizorForm(instance=furnizor)
	return render(request,'orderhelper/modal_dialog.html', {'form': form, 'dialog_title':dialog_title, 'url': url})

@login_required
def proiect_new(request):
	dialog_title = 'Adauga proiect'
	url = '/proiect/new/'

	if request.method == "POST":
		form = ProiectForm(request.POST)
		if form.is_valid():
			proiect = form.save(commit=True)
			proiect.save()
			return redirect(request.META['HTTP_REFERER'])
	
	form = ProiectForm()
	return render(request,'orderhelper/modal_dialog.html', {'form': form, 'dialog_title':dialog_title, 'url':url})

@login_required
def proiect_edit(request, pk):
	proiect = get_object_or_404(Proiect, pk=pk)
	dialog_title = 'Editeaza proiect'
	url = '/proiect/edit/' + pk

	if request.method == "POST":
		form = ProiectForm(request.POST,instance=proiect)
		if form.is_valid():
			proiect = form.save(commit=True)
			proiect.save()
			return redirect(request.META['HTTP_REFERER'])
	
	form = ProiectForm(instance=proiect)
	return render(request,'orderhelper/modal_dialog.html', {'form': form, 'dialog_title':dialog_title, 'url':url})

@login_required
def persoana_new(request):
	dialog_title = 'Adauga solicitant'
	url = '/persoana/new/'

	if request.method == "POST":
		form = PersoanaForm(request.POST)
		if form.is_valid():
			persoana = form.save(commit=True)
			persoana.save()
			return redirect(request.META['HTTP_REFERER'])
	
	form = PersoanaForm()
	return render(request,'orderhelper/modal_dialog.html', {'form': form, 'dialog_title':dialog_title, 'url':url})

@login_required
def producator_edit(request, pk):
	producator = get_object_or_404(Producator, pk=pk)
	dialog_title = 'Editeaza producator'
	url = '/producator/edit/' + pk
	if request.method == "POST":
		form = ProducatorForm(request.POST,instance=producator)
		if form.is_valid():
			producator = form.save(commit=True)
			producator.save()
			return redirect(request.META['HTTP_REFERER'])

	form = ProducatorForm(instance=producator)
	return render(request,'orderhelper/modal_dialog.html', {'form': form, 'dialog_title':dialog_title, 'url':url})

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

@login_required
def comanda_detail(request, pk):
	comanda = get_object_or_404(Comanda, pk=pk)

	return render(request,'orderhelper/comanda_detail.html', {'comanda':comanda})

@login_required
def subcomanda_detail(request, pk):
	subcomanda = get_object_or_404(Subcomanda, pk=pk)

	return render(request,'orderhelper/subcomanda_detail.html', {'subcomanda':subcomanda})


