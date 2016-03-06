from django.conf.urls import patterns, include, url
from . import views


urlpatterns = [
	url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^pending_comanda/$', views.pending_comanda, name='pending_comanda'),
    url(r'^comanda/(?P<pk>[0-9]+)/$', views.comanda_subcomenzi, name='comanda_subcomenzi'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^order_history$', views.order_history, name='order_history'),
    url(r'^proiect/all/$', views.proiect_all, name='proiect_all'),
    url(r'^furnizor/all/$', views.furnizor_all, name='furnizor_all'),
    url(r'^producator/all/$', views.producator_all, name='producator_all'),
    url(r'^reper/all/$', views.reper_all, name='reper_all'),
    url(r'^logout/$', views.logout_page, name='logout_page'),
    url(r'^comanda/all/$', views.comanda_all, name='comanda_all'),
    url(r'^subcomanda/all/$', views.subcomanda_all, name='subcomanda_all'),
    url(r'^comanda/new/$', views.comanda_new, name='comanda_new'),
    url(r'^subcomanda/new/$', views.subcomanda_new, name='subcomanda_new'),
    url(r'^subcomanda/(?P<pk>\d+)/edit/$', views.subcomanda_edit, name='subcomanda_edit'),
    url(r'^comanda/(?P<pk>\d+)/edit/$', views.comanda_edit, name='comanda_edit'),
    url(r'^reper/new/$', views.reper_new, name='reper_new'),
    url(r'^producator/new/$', views.producator_new, name='producator_new'),
    url(r'^furnizor/new/$', views.furnizor_new, name='furnizor_new'),
    url(r'^proiect/new/$', views.proiect_new, name='proiect_new'),
    url(r'^persoana/new/$', views.persoana_new, name='persoana_new'),
    url(r'^producator/edit/(?P<pk>\d+)$', views.producator_edit, name='producator_edit'),
    url(r'^subcomanda/close/(?P<pk>\d+)$', views.pending_subcomanda_close, name='pending_subcomanda_close'),
    url(r'^comanda/close/(?P<pk>\d+)$', views.pending_comanda_close, name='pending_comanda_close'),
    url(r'^subcomanda/cancel/(?P<pk>\d+)$', views.pending_subcomanda_cancel, name='pending_subcomanda_cancel'),
    url(r'^comanda/cancel/(?P<pk>\d+)$', views.pending_comanda_cancel, name='pending_comanda_cancel'),
]