from django.conf.urls import patterns, include, url
from . import views
from .views import PendingView, DashboardView, HistoryView,SearchView, DashboardProiectView, DashboardFurnizorView, DashboardProducatorView, DashboardReperView, DashboardComandaView, DashboardComandaCreateView, DashboardPersoanaCreateView, DashboardProiectCreateView, DashboardFurnizorCreateView, DashboardProducatorCreateView, DashboardReperCreateView, DashboardSubcomandaCreateView, DashboardSubcomandaView


urlpatterns = [
	
    # url(r'^comanda/(?P<pk>[0-9]+)/$', views.comanda_subcomenzi, name='comanda_subcomenzi'),

    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', views.logout_page, name='logout_page'), 

    # Pending 
    url(r'^pending/$', PendingView.as_view(), name='pending'),

    # Comanda/Subcomanda urls used Pending & History
    url(r'^subcomanda/close/(?P<pk>\d+)$', views.pending_subcomanda_close, name='pending_subcomanda_close'),
    url(r'^comanda/close/(?P<pk>\d+)$', views.pending_comanda_close, name='pending_comanda_close'),
    url(r'^subcomanda/cancel/(?P<pk>\d+)$', views.pending_subcomanda_cancel, name='pending_subcomanda_cancel'),
    url(r'^comanda/cancel/(?P<pk>\d+)$', views.pending_comanda_cancel, name='pending_comanda_cancel'),
    url(r'^comanda/detail/(?P<pk>\d+)$', views.comanda_detail, name='comanda_detail'),
    url(r'^subcomanda/detail/(?P<pk>\d+)$', views.subcomanda_detail, name='subcomanda_detail'),

    # Dashboard
    url(r'^dashboard/$', DashboardView.as_view() , name='dashboard'),
    url(r'^dashboard/comanda/$', DashboardComandaView.as_view() , name='dashboard_comanda'),
    url(r'^dashboard/subcomanda/$', DashboardSubcomandaView.as_view() , name='dashboard_subcomanda'),
    url(r'^dashboard/proiect/$', DashboardProiectView.as_view() , name='dashboard_proiect'),
    url(r'^dashboard/furnizor/$', DashboardFurnizorView.as_view() , name='dashboard_furnizor'),
    url(r'^dashboard/producator/$', DashboardProducatorView.as_view() , name='dashboard_producator'),
    url(r'^dashboard/reper/$', DashboardReperView.as_view(), name='dashboard_reper'),
    url(r'^dashboard/comanda/new/$', DashboardComandaCreateView.as_view(), name='dashboard_comanda_new'),
    url(r'^dashboard/comanda/edit/(?P<pk>\d+)$', views.dashboard_comanda_edit, name='dashboard_comanda_edit'),
    url(r'^dashboard/subcomanda/new/$', DashboardSubcomandaCreateView.as_view(), name='dashboard_subcomanda_new'),
    url(r'^dashboard/subcomanda/edit/(?P<pk>\d+)$', views.dashboard_subcomanda_edit, name='dashboard_subcomanda_edit'),

    # Modal dialogs for dashboard
    url(r'^reper/new/$', DashboardReperCreateView.as_view() , name='reper_new'),
    url(r'^reper/edit/(?P<pk>\d+)$', views.reper_edit, name='reper_edit'),
    url(r'^producator/new/$', DashboardProducatorCreateView.as_view() , name='producator_new'),
    url(r'^producator/edit/(?P<pk>\d+)$', views.producator_edit, name='producator_edit'),
    url(r'^furnizor/new/$', DashboardFurnizorCreateView.as_view() , name='furnizor_new'),
    url(r'^furnizor/edit/(?P<pk>\d+)$', views.furnizor_edit, name='furnizor_edit'),
    url(r'^proiect/new/$', DashboardProiectCreateView.as_view() , name='proiect_new'),
    url(r'^proiect/edit/(?P<pk>\d+)$', views.proiect_edit, name='proiect_edit'),
    url(r'^persoana/new/$', DashboardPersoanaCreateView.as_view() , name='persoana_new'),
   
    # History 
    url(r'^history$', HistoryView.as_view(), name='history'),   

    # Search
    url(r'^search$', SearchView.as_view(), name='search'),  
     
   
   
    
]