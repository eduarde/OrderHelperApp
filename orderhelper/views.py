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
	paginate_by = 10

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(DashboardProiectView, self).dispatch(*args, **kwargs)

	def get_queryset(self):
		groups_list = self.request.user.groups.all()
		return Proiect.objects.all().filter(group__in=groups_list).order_by('-pk')

# Furnizor view in Dashboard 
class DashboardFurnizorView(PaginationMixin, ListView):
	model = Furnizor
	template_name = 'orderhelper/dashboard_furnizor.html'
	context_object_name = 'furnizori'
	paginate_by = 10


	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(DashboardFurnizorView, self).dispatch(*args, **kwargs)

	def get_queryset(self):
		groups_list = self.request.user.groups.all()
		return Furnizor.objects.all().filter(group__in=groups_list).order_by('-pk')

# Producator view in Dashboard 
class DashboardProducatorView(PaginationMixin, ListView):
	model = Producator
	template_name = 'orderhelper/dashboard_producator.html'
	context_object_name = 'producatori'
	paginate_by = 10

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(DashboardProducatorView, self).dispatch(*args, **kwargs)

	def get_queryset(self):
		groups_list = self.request.user.groups.all()
		return  Producator.objects.all().filter(group__in=groups_list).order_by('-pk')

# Reper view in Dashboard 
class DashboardReperView(PaginationMixin, ListView):
	model = Reper
	template_name = 'orderhelper/dashboard_reper.html'
	context_object_name = 'reperi'
	paginate_by = 10

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(DashboardReperView, self).dispatch(*args, **kwargs)

	def get_queryset(self):
		groups_list = self.request.user.groups.all()
		return Reper.objects.all().filter(group__in=groups_list).order_by('-pk')

# Reper view in Dashboard 
class DashboardReperModalView(PaginationMixin, ListView):
	model = Reper
	template_name = 'orderhelper/dashboard_reper_view.html'
	context_object_name = 'reperi'
	paginate_by = 1000

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(DashboardReperModalView, self).dispatch(*args, **kwargs)

	def get_queryset(self):
		groups_list = self.request.user.groups.all()
		return Reper.objects.all().filter(group__in=groups_list).order_by('-pk')


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

# Comanda edit view
class DashboardComandaEditView(FormView):

	template_name = 'orderhelper/dashboard_comanda_edit.html'
	success_url = 'dashboard_comanda';
	form_class = ComandaEditForm

	@method_decorator(login_required)
	def get(self, request, *args, **kwargs):
		self.object = self.get_object();		
		form = self.form_class(instance=self.object)
		return render(request, self.template_name, {'comandaform': form})

	def get_object(self):
		return get_object_or_404(Comanda, pk=self.kwargs.get("pk"))
	
	@method_decorator(login_required)
	def post(self, request, *args, **kwargs):
		self.object = self.get_object();
		form = self.form_class(request.POST,instance=self.object)
		if form.is_valid():
			self.object = form.save(commit=True)
			self.object.save()
			return redirect(self.success_url)
	
		return render(request, self.template_name, {'comandaform': form})


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


# Subcomanda edit view
class DashboardSubcomandaEditView(FormView):

	template_name = 'orderhelper/dashboard_subcomanda_edit.html'
	success_url = 'dashboard_subcomanda';
	form_class = SubcomandaEditForm

	@method_decorator(login_required)
	def get(self, request, *args, **kwargs):
		self.object = self.get_object();		
		form = self.form_class(instance=self.object)
		return render(request, self.template_name, {'subcomandaform': form})

	def get_object(self):
		return get_object_or_404(Subcomanda, pk=self.kwargs.get("pk"))

	@method_decorator(login_required)
	def post(self, request, *args, **kwargs):
		self.object = self.get_object();
		form = self.form_class(request.POST,instance=self.object)
		if form.is_valid():
			self.object = form.save(commit=True)
			self.object.save()
			return redirect(self.success_url)
	
		return render(request, self.template_name, {'subcomandaform': form})


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


# Reper edit view
class DashboardReperEditView(FormView):

	template_name = 'orderhelper/modal_dialog.html'
	form_class = ReperForm
	dialog_title = "Editeaza reper"
	
	@method_decorator(login_required)
	def get(self, request, *args, **kwargs):
		url = '/reper/edit/' + self.get_primary_key()
		self.object = self.get_object()
		form = self.form_class(instance=self.object)
		return render(request, self.template_name, {'form': form, 'dialog_title': self.dialog_title, 'url': url})

	def get_object(self):
		return get_object_or_404(Reper, pk=self.kwargs.get("pk"))	

	def get_primary_key(self):
		return self.kwargs.get("pk")	

	@method_decorator(login_required)
	def post(self, request, *args, **kwargs):
		url = '/reper/edit/' + self.get_primary_key()
		self.object = self.get_object();
		form = self.form_class(request.POST,instance=self.object)
		if form.is_valid():
			self.object = form.save(commit=True)
			self.object.save()
			return redirect(request.META['HTTP_REFERER'])
	
		return render(request, self.template_name, {'form': form, 'dialog_title': self.dialog_title, 'url': url})

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


# Furnizor edit view
class DashboardFurnizorEditView(FormView):

	template_name = 'orderhelper/modal_dialog.html'
	form_class = FurnizorForm
	dialog_title = "Editeaza furnizor"
	
	@method_decorator(login_required)
	def get(self, request, *args, **kwargs):
		url = '/furnizor/edit/' + self.get_primary_key()
		self.object = self.get_object()
		form = self.form_class(instance=self.object)
		return render(request, self.template_name, {'form': form, 'dialog_title': self.dialog_title, 'url': url})

	def get_object(self):
		return get_object_or_404(Furnizor, pk=self.kwargs.get("pk"))	

	def get_primary_key(self):
		return self.kwargs.get("pk")	

	@method_decorator(login_required)
	def post(self, request, *args, **kwargs):
		url = '/furnizor/edit/' + self.get_primary_key()
		self.object = self.get_object();
		form = self.form_class(request.POST,instance=self.object)
		if form.is_valid():
			self.object = form.save(commit=True)
			self.object.save()
			return redirect(request.META['HTTP_REFERER'])
	
		return render(request, self.template_name, {'form': form, 'dialog_title': self.dialog_title, 'url': url})

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

# Proiect edit view
class DashboardProiectEditView(FormView):

	template_name = 'orderhelper/modal_dialog.html'
	form_class = ProiectForm
	dialog_title = "Editeaza proiect"
	
	@method_decorator(login_required)
	def get(self, request, *args, **kwargs):
		url = '/proiect/edit/' + self.get_primary_key()
		self.object = self.get_object()
		form = self.form_class(instance=self.object)
		return render(request, self.template_name, {'form': form, 'dialog_title': self.dialog_title, 'url': url})

	def get_object(self):
		return get_object_or_404(Proiect, pk=self.kwargs.get("pk"))	

	def get_primary_key(self):
		return self.kwargs.get("pk")	

	@method_decorator(login_required)
	def post(self, request, *args, **kwargs):
		url = '/proiect/edit/' + self.get_primary_key()
		self.object = self.get_object();
		form = self.form_class(request.POST,instance=self.object)
		if form.is_valid():
			self.object = form.save(commit=True)
			self.object.save()
			return redirect(request.META['HTTP_REFERER'])
	
		return render(request, self.template_name, {'form': form, 'dialog_title': self.dialog_title, 'url': url})


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


# Producator edit view
class DashboardProducatorEditView(FormView):

	template_name = 'orderhelper/modal_dialog.html'
	form_class = ProducatorForm
	dialog_title = "Editeaza producator"
	
	@method_decorator(login_required)
	def get(self, request, *args, **kwargs):
		url = '/producator/edit/' + self.get_primary_key()
		self.object = self.get_object()
		form = self.form_class(instance=self.object)
		return render(request, self.template_name, {'form': form, 'dialog_title': self.dialog_title, 'url': url})

	def get_object(self):
		return get_object_or_404(Producator, pk=self.kwargs.get("pk"))	

	def get_primary_key(self):
		return self.kwargs.get("pk")	

	@method_decorator(login_required)
	def post(self, request, *args, **kwargs):
		url = '/producator/edit/' + self.get_primary_key()
		self.object = self.get_object();
		form = self.form_class(request.POST,instance=self.object)
		if form.is_valid():
			self.object = form.save(commit=True)
			self.object.save()
			return redirect(request.META['HTTP_REFERER'])
	
		return render(request, self.template_name, {'form': form, 'dialog_title': self.dialog_title, 'url': url})

# Pending subcomanda close view
class PendingSubcomandaCloseView(FormView):

	template_name = 'orderhelper/pending_modal_edit.html'
	form_class = SubcomandaCloseForm
	dialog_title = "Inchide subcomanda"
	
	@method_decorator(login_required)
	def get(self, request, *args, **kwargs):
		url = '/subcomanda/close/' + self.get_primary_key()
		self.object = self.get_object()
		form = self.form_class(instance=self.object)
		return render(request, self.template_name, {'form': form, 'subcomanda': self.object, 'dialog_title': self.dialog_title, 'url': url})

	def get_object(self):
		return get_object_or_404(Subcomanda, pk=self.kwargs.get("pk"))	

	def get_primary_key(self):
		return self.kwargs.get("pk")	

	@method_decorator(login_required)
	def post(self, request, *args, **kwargs):
		url = '/subcomanda/close/' + self.get_primary_key()
		self.object = self.get_object();
		form = self.form_class(request.POST,instance=self.object)
		if form.is_valid():
			self.object = form.save(commit=False)
			self.object.status = Status.objects.filter(text='Inchis')[0]
			self.object.save()
			return redirect(request.META['HTTP_REFERER'])
	
		return render(request, self.template_name, {'form': form, 'subcomanda': self.object, 'dialog_title': self.dialog_title, 'url': url})

# Pending comanda close view
class PendingComandaCloseView(FormView):

	template_name = 'orderhelper/pending_modal_edit.html'
	form_class = ComandaCloseForm
	dialog_title = "Inchide comanda"
	
	@method_decorator(login_required)
	def get(self, request, *args, **kwargs):
		url = '/comanda/close/' + self.get_primary_key()
		self.object = self.get_object()
		form = self.form_class(instance=self.object)
		return render(request, self.template_name, {'form': form, 'comanda': self.object, 'dialog_title': self.dialog_title, 'url': url})

	def get_object(self):
		return get_object_or_404(Comanda, pk=self.kwargs.get("pk"))	

	def get_primary_key(self):
		return self.kwargs.get("pk")	

	@method_decorator(login_required)
	def post(self, request, *args, **kwargs):
		url = '/comanda/close/' + self.get_primary_key()
		self.object = self.get_object();
		form = self.form_class(request.POST,instance=self.object)
		if form.is_valid():
			self.object = form.save(commit=False)
			self.object.status = Status.objects.filter(text='Inchis')[0]
			self.object.save()
			return redirect(request.META['HTTP_REFERER'])
	
		return render(request, self.template_name, {'form': form, 'comanda': self.object, 'dialog_title': self.dialog_title, 'url': url})

# Pending subcomanda cancel view
class PendingSubcomandaCancelView(ListView):

	template_name = 'orderhelper/pending_modal_cancel.html'
	dialog_title = "Anuleaza subcomanda"
	content = "Sunteti sigur ca doriti sa anulati aceasta subcomanda?"
	
	@method_decorator(login_required)
	def get(self, request, *args, **kwargs):
		url = '/subcomanda/cancel/' + self.get_primary_key()
		self.object = self.get_object()
		return render(request, self.template_name, {'subcomanda': self.object,'content': self.content, 'dialog_title': self.dialog_title, 'url': url})

	def get_object(self):
		return get_object_or_404(Subcomanda, pk=self.kwargs.get("pk"))	

	def get_primary_key(self):
		return self.kwargs.get("pk")	

	@method_decorator(login_required)
	def post(self, request, *args, **kwargs):
		url = '/subcomanda/cancel/' + self.get_primary_key()
		self.object = self.get_object();
		self.object.status = Status.objects.filter(text='Anulat')[0]
		self.object.save()	
		return redirect(request.META['HTTP_REFERER'])
		

# Pending comanda cancel view
class PendingComandaCancelView(ListView):

	template_name = 'orderhelper/pending_modal_cancel.html'
	dialog_title = "Anuleaza comanda"
	content = "Sunteti sigur ca doriti sa anulati aceasta comanda? Subcomenzile asociate acestei comenzi se vor anula implicit."
	
	@method_decorator(login_required)
	def get(self, request, *args, **kwargs):
		url = '/comanda/cancel/' + self.get_primary_key()
		self.object = self.get_object()
		return render(request, self.template_name, {'comanda': self.object,'content':self.content, 'dialog_title': self.dialog_title, 'url': url})

	def get_object(self):
		return get_object_or_404(Comanda, pk=self.kwargs.get("pk"))	

	def get_primary_key(self):
		return self.kwargs.get("pk")	

	@method_decorator(login_required)
	def post(self, request, *args, **kwargs):
		url = '/comanda/cancel/' + self.get_primary_key()
		status_anulat = Status.objects.filter(text='Anulat')[0]
		self.object = self.get_object();
		self.object.status = status_anulat
		self.object.save()
		subcomenzi = Subcomanda.objects.filter(comanda_ref__pk=self.get_primary_key())
		for subcomanda in subcomenzi:
			subcomanda.status = status_anulat
			subcomanda.save()	
		return redirect(request.META['HTTP_REFERER'])

# Comanda detail view displayed in modal
class ComandaDetailView(ListView):
	template_name = 'orderhelper/comanda_detail.html'
	
	@method_decorator(login_required)
	def get(self, request, *args, **kwargs):
		self.object = self.get_object()
		return render(request, self.template_name, {'comanda': self.object})

	def get_object(self):
		return get_object_or_404(Comanda, pk=self.kwargs.get("pk"))	


# Subcomanda detail view displayed in modal
class SubcomandaDetailView(ListView):
	template_name = 'orderhelper/subcomanda_detail.html'
	
	@method_decorator(login_required)
	def get(self, request, *args, **kwargs):
		self.object = self.get_object()
		return render(request, self.template_name, {'subcomanda': self.object})

	def get_object(self):
		return get_object_or_404(Subcomanda, pk=self.kwargs.get("pk"))	

# Search view class
class SearchView(PaginationMixin, ListView):
	model = Subcomanda
	template_name = 'orderhelper/search.html'
	context_object_name = 'subcomenzi'
	paginate_by = 5
	cod_reper_text = ''
	reper_text = ''
	furnizor_text = ''
	proiect_text = ''
	obiect_text = ''
	qlist = []

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(SearchView, self).dispatch(*args, **kwargs)

	def build_queries(self):
		qlist = []
		if self.cod_reper_text != 'none':
			qlist.append(Q(reper__cod_reper__icontains=self.cod_reper_text))
		if self.reper_text != 'none':
			qlist.append(Q(reper__reper__icontains=self.reper_text))
		if self.furnizor_text != 'none':	
			qlist.append(Q(furnizor__nume__icontains=self.furnizor_text))
		if self.proiect_text != 'none':	
			qlist.append(Q(comanda_ref__proiect__titlu__icontains=self.proiect_text))
		if self.obiect_text != 'none':	
			qlist.append(Q(comanda_ref__obiect_succint__icontains=self.obiect_text))

		return qlist

	def get_queryset(self):
		self.cod_reper_text = self.kwargs.get("cod_reper_text")
		self.reper_text = self.kwargs.get("reper_text")
		self.furnizor_text = self.kwargs.get("furnizor_text")
		self.proiect_text = self.kwargs.get("proiect_text")
		self.obiect_text = self.kwargs.get("obiect_text")

		qlist = self.build_queries()
		print(qlist)
		if qlist:
			return Subcomanda.objects.filter(reduce(AND, qlist))
		else:
			return Subcomanda.objects.all()




