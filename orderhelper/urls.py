from django.conf.urls import patterns, include, url
from . import views


urlpatterns = [
	url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^pending_comanda/$', views.pending_comanda, name='pending_comanda'),
    url(r'^comanda/(?P<pk>[0-9]+)/$', views.comanda_subcomenzi, name='comanda_subcomenzi'),

    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^dashboard/comanda/$', views.dashboard_comanda, name='dashboard_comanda'),
    url(r'^dashboard/subcomanda/$', views.dashboard_subcomanda, name='dashboard_subcomanda'),
    url(r'^dashboard/proiect/$', views.dashboard_proiect, name='dashboard_proiect'),
    url(r'^dashboard/furnizor/$', views.dashboard_furnizor, name='dashboard_furnizor'),
    url(r'^dashboard/producator/$', views.dashboard_producator, name='dashboard_producator'),
    url(r'^dashboard/reper/$', views.dashboard_reper, name='dashboard_reper'),
    url(r'^dashboard/comanda/new/$', views.dashboard_comanda_new, name='dashboard_comanda_new'),
    url(r'^dashboard/comanda/edit/(?P<pk>\d+)$', views.dashboard_comanda_edit, name='dashboard_comanda_edit'),
    url(r'^dashboard/subcomanda/new/$', views.dashboard_subcomanda_new, name='dashboard_subcomanda_new'),
    url(r'^dashboard/subcomanda/edit/(?P<pk>\d+)$', views.dashboard_subcomanda_edit, name='dashboard_subcomanda_edit'),

    url(r'^reper/new/$', views.reper_new, name='reper_new'),
    url(r'^reper/edit/(?P<pk>\d+)$', views.reper_edit, name='reper_edit'),
    url(r'^producator/new/$', views.producator_new, name='producator_new'),
    url(r'^producator/edit/(?P<pk>\d+)$', views.producator_edit, name='producator_edit'),
    url(r'^furnizor/new/$', views.furnizor_new, name='furnizor_new'),
    url(r'^furnizor/edit/(?P<pk>\d+)$', views.furnizor_edit, name='furnizor_edit'),
    url(r'^proiect/new/$', views.proiect_new, name='proiect_new'),
    url(r'^proiect/edit/(?P<pk>\d+)$', views.proiect_edit, name='proiect_edit'),
    url(r'^persoana/new/$', views.persoana_new, name='persoana_new'),
   
    url(r'^order_history$', views.order_history, name='order_history'),    
    url(r'^logout/$', views.logout_page, name='logout_page'),   
   
   
    url(r'^subcomanda/close/(?P<pk>\d+)$', views.pending_subcomanda_close, name='pending_subcomanda_close'),
    url(r'^comanda/close/(?P<pk>\d+)$', views.pending_comanda_close, name='pending_comanda_close'),
    url(r'^subcomanda/cancel/(?P<pk>\d+)$', views.pending_subcomanda_cancel, name='pending_subcomanda_cancel'),
    url(r'^comanda/cancel/(?P<pk>\d+)$', views.pending_comanda_cancel, name='pending_comanda_cancel'),
    url(r'^comanda/detail/(?P<pk>\d+)$', views.comanda_detail, name='comanda_detail'),
    url(r'^subcomanda/detail/(?P<pk>\d+)$', views.subcomanda_detail, name='subcomanda_detail'),
]