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
from django.http import HttpResponse
from django.views.generic import View, ListView
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from pure_pagination.mixins import PaginationMixin
from django.db.models import Q
from operator import __and__ as AND
from functools import reduce

# def handler404(request):
# 	return render(request,'orderhelper/error404.html');

@login_required
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

# Dashboard view 
class DashboardView(View):
	template_name = 'orderhelper/dashboard.html'

	@method_decorator(login_required)
	def get(self, request):
		return render(request, self.template_name)

# Pending view 
class PendingView(ListView):
	model = Comanda
	template_name = 'orderhelper/pending.html'
	context_object_name = 'comenzi'

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(PendingView, self).dispatch(*args, **kwargs)
	
	def get_queryset(self):
		groups_list = self.request.user.groups.all()
		return Comanda.objects.all().filter(status__text='Deschis',group__in=groups_list).order_by('data')

# History view 
class HistoryView(PaginationMixin, ListView):
	model = Comanda
	template_name = 'orderhelper/history.html'
	context_object_name = 'comenzi'
	paginate_by = 10

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(HistoryView, self).dispatch(*args, **kwargs)

	def get_queryset(self):
		groups_list = self.request.user.groups.all()
		return Comanda.objects.all().filter(status__text='Inchis',group__in=groups_list).order_by('data')

# Comanda view in Dashboard 
class DashboardComandaView(PaginationMixin, ListView):
	model = Comanda
	template_name = 'orderhelper/dashboard_comanda.html'
	context_object_name = 'comenzi'
	paginate_by = 8

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(DashboardComandaView, self).dispatch(*args, **kwargs)

	def get_queryset(self):
		groups_list = self.request.user.groups.all()
		return Comanda.objects.all().filter(group__in=groups_list,data__gte=datetime.now()-timedelta(days=30)).order_by('-data')

# Subcomanda view in Dashboard 
class DashboardSubcomandaView(PaginationMixin, ListView):
	model = Subcomanda
	template_name = 'orderhelper/dashboard_subcomanda.html'
	context_object_name = 'subcomenzi'
	paginate_by = 6

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(DashboardSubcomandaView, self).dispatch(*args, **kwargs)

	def get_queryset(self):
		groups_list = self.request.user.groups.all()
		return Subcomanda.objects.all().filter(group__in=groups_list,data__gte=datetime.now()-timedelta(days=30)).order_by('-data')


# Proiect view in Dashboard 
class DashboardProiectView(PaginationMixin, ListView):
	model = Proiect
	template_name = 'orderhelper/dashboard_proiect.html'
	context_object_name = 'proiecte'
	paginate_by = 8

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(DashboardProiectView, self).dispatch(*args, **kwargs)

	def get_queryset(self):
		groups_list = self.request.user.groups.all()
		return Proiect.objects.all().filter(group__in=groups_list).order_by('pk')

# Furnizor view in Dashboard 
class DashboardFurnizorView(PaginationMixin, ListView):
	model = Furnizor
	template_name = 'orderhelper/dashboard_furnizor.html'
	context_object_name = 'furnizori'
	paginate_by = 8


	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(DashboardFurnizorView, self).dispatch(*args, **kwargs)

	def get_queryset(self):
		groups_list = self.request.user.groups.all()
		return Furnizor.objects.all().filter(group__in=groups_list).order_by('pk')

# Producator view in Dashboard 
class DashboardProducatorView(PaginationMixin, ListView):
	model = Producator
	template_name = 'orderhelper/dashboard_producator.html'
	context_object_name = 'producatori'
	paginate_by = 8

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(DashboardProducatorView, self).dispatch(*args, **kwargs)

	def get_queryset(self):
		groups_list = self.request.user.groups.all()
		return  Producator.objects.all().filter(group__in=groups_list).order_by('pk')

# Reper view in Dashboard 
class DashboardReperView(PaginationMixin, ListView):
	model = Reper
	template_name = 'orderhelper/dashboard_reper.html'
	context_object_name = 'reperi'
	paginate_by = 5

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(DashboardReperView, self).dispatch(*args, **kwargs)

	def get_queryset(self):
		groups_list = self.request.user.groups.all()
		return Reper.objects.all().filter(group__in=groups_list).order_by('pk')	


# Comanda create view
class DashboardComandaCreateView(FormView):

	template_name = 'orderhelper/dashboard_comanda_new.html'
	success_url = 'dashboard_comanda';
	form_class = ComandaForm

	@method_decorator(login_required)
	def get(self, request, *args, **kwargs):
		form = self.form_class()
		return render(request, self.template_name, {'comandaform': form})
	
	@method_decorator(login_required)
	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			self.object = form.save(commit=False)
			self.object.status = Status.objects.all().filter(text='Deschis')[0]
			self.object.data = datetime.now()
			self.object.preluat = self.request.user
			self.object.save()
			form.save_m2m()
			return redirect(self.success_url)
	
		return render(request, self.template_name, {'comandaform': form})


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



# Subcomanda create view
class DashboardSubcomandaCreateView(FormView):

	template_name = 'orderhelper/dashboard_subcomanda_new.html'
	success_url = 'dashboard_subcomanda';
	form_class = SubcomandaForm

	@method_decorator(login_required)
	def get(self, request, *args, **kwargs):
		form = self.form_class()
		return render(request, self.template_name, {'subcomandaform': form})
	
	def calculate_numar_curent(self):
		numar_curent = 0
		if Subcomanda.objects.all().filter(comanda_ref__numar_unic=self.object.comanda_ref.numar_unic).exists(): 
				numar_curent = Subcomanda.objects.all().filter(comanda_ref__numar_unic=self.object.comanda_ref.numar_unic).latest('pk').numar_curent
		numar_curent = numar_curent + 1
		return numar_curent

	@method_decorator(login_required)
	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			self.object = form.save(commit=False)
			self.object.status = Status.objects.all().filter(text='Deschis')[0]
			self.object.numar_curent = self.calculate_numar_curent()
			self.object.data = datetime.now()
			self.object.save()
			form.save_m2m()
			return redirect(self.success_url)
	
		return render(request, self.template_name, {'subcomandaform': form})


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


# Reper create view
class DashboardReperCreateView(FormView):

	template_name = 'orderhelper/modal_dialog.html'
	form_class = ReperForm
	dialog_title = 'Adauga reper'
	url = '/reper/new/'

	@method_decorator(login_required)
	def get(self, request, *args, **kwargs):
		form = self.form_class()
		return render(request, self.template_name, {'form': form, 'dialog_title': self.dialog_title, 'url': self.url})

	@method_decorator(login_required)
	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			self.object = form.save(commit=True)
			self.object.save()
			return redirect(request.META['HTTP_REFERER'])
	
		return render(request, self.template_name, {'form': form, 'dialog_title': self.dialog_title, 'url': self.url})


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


# Producator create view
class DashboardProducatorCreateView(FormView):

	template_name = 'orderhelper/modal_dialog.html'
	form_class = ProducatorForm
	dialog_title = 'Adauga producator'
	url = '/producator/new/'

	@method_decorator(login_required)
	def get(self, request, *args, **kwargs):
		form = self.form_class()
		return render(request, self.template_name, {'form': form, 'dialog_title': self.dialog_title, 'url': self.url})

	@method_decorator(login_required)
	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			self.object = form.save(commit=True)
			self.object.save()
			return redirect(request.META['HTTP_REFERER'])
	
		return render(request, self.template_name, {'form': form, 'dialog_title': self.dialog_title, 'url': self.url})


#Furnizor create view
class DashboardFurnizorCreateView(FormView):

	template_name = 'orderhelper/modal_dialog.html'
	form_class = FurnizorForm
	dialog_title = 'Adauga furnizor'
	url = '/furnizor/new/'

	@method_decorator(login_required)
	def get(self, request, *args, **kwargs):
		form = self.form_class()
		return render(request, self.template_name, {'form': form, 'dialog_title': self.dialog_title, 'url': self.url})

	@method_decorator(login_required)
	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			self.object = form.save(commit=True)
			self.object.save()
			return redirect(request.META['HTTP_REFERER'])
	
		return render(request, self.template_name, {'form': form, 'dialog_title': self.dialog_title, 'url': self.url})


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


# Proiect create view
class DashboardProiectCreateView(FormView):

	template_name = 'orderhelper/modal_dialog.html'
	form_class = ProiectForm
	dialog_title = 'Adauga proiect'
	url = '/proiect/new/'

	@method_decorator(login_required)
	def get(self, request, *args, **kwargs):
		form = self.form_class()
		return render(request, self.template_name, {'form': form, 'dialog_title': self.dialog_title, 'url': self.url})

	@method_decorator(login_required)
	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			self.object = form.save(commit=True)
			self.object.save()
			return redirect(request.META['HTTP_REFERER'])
	
		return render(request, self.template_name, {'form': form, 'dialog_title': self.dialog_title, 'url': self.url})

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


# Persoana create view
class DashboardPersoanaCreateView(FormView):

	template_name = 'orderhelper/modal_dialog.html'
	form_class = PersoanaForm
	dialog_title = 'Adauga solicitant'
	url = '/persoana/new/'

	@method_decorator(login_required)
	def get(self, request, *args, **kwargs):
		form = self.form_class()
		return render(request, self.template_name, {'form': form, 'dialog_title': self.dialog_title, 'url': self.url})

	@method_decorator(login_required)
	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			self.object = form.save(commit=True)
			self.object.save()
			return redirect(request.META['HTTP_REFERER'])
	
		return render(request, self.template_name, {'form': form, 'dialog_title': self.dialog_title, 'url': self.url})


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

@login_required
def search_view(request, reper_text, furnizor_text, producator_text):

	qlist = []
	if reper_text != 'qnz':
		qlist.append(Q(reper__reper__icontains=reper_text) | Q(reper__cod_reper__icontains=reper_text))
	if furnizor_text != 'qnz':	
		qlist.append(Q(furnizor__nume__icontains=furnizor_text))
	if producator_text != 'qnz':	
		qlist.append(Q(producator__nume__icontains=producator_text))

	if qlist:
		subcomenzi = Subcomanda.objects.filter(reduce(AND, qlist))
	else:
		subcomenzi = Subcomanda.objects.all()
	return render(request,'orderhelper/search.html',{'subcomenzi':subcomenzi, 'reper_text':reper_text})

class SearchView(PaginationMixin, ListView):
	model = Subcomanda
	template_name = 'orderhelper/search.html'
	context_object_name = 'subcomenzi'
	paginate_by = 8

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(SearchView, self).dispatch(*args, **kwargs)
	
	def get_queryset(self):
		groups_list = self.request.user.groups.all()
		return Subcomanda.objects.all().filter(group__in=groups_list).order_by('data')



