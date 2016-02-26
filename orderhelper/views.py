from django.shortcuts import render, get_object_or_404
from .models import Comanda, Subcomanda
from .forms import PersoanaForm
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
