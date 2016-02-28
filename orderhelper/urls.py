from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
	url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^pending_comanda/$', views.pending_comanda, name='pending_comanda'),
    url(r'^comanda/(?P<pk>[0-9]+)/$', views.comanda_subcomenzi, name='comanda_subcomenzi'),
    url(r'^persoana/new/$', views.persoana_new, name='persoana_new'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^order_history$', views.order_history, name='order_history'),
    url(r'^proiect/all/$', views.proiect_all, name='proiect_all'),
    url(r'^furnizor/all/$', views.furnizor_all, name='furnizor_all'),
    url(r'^producator/all/$', views.producator_all, name='producator_all'),
    url(r'^reper/all/$', views.reper_all, name='reper_all'),
    url(r'^logout/$', views.logout_page, name='logout_page'),
    url(r'^comanda/all/$', views.comanda_all, name='comanda_all'),
    url(r'^subcomanda/all/$', views.subcomanda_all, name='subcomanda_all'),
]