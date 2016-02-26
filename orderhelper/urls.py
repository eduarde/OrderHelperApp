from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
	url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^pending_comanda/$', views.pending_comanda, name='pending_comanda'),
    url(r'^comanda/(?P<pk>[0-9]+)/$', views.comanda_subcomenzi, name='comanda_subcomenzi'),
    url(r'^persoana/new/$', views.persoana_new, name='persoana_new'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^order_history$', views.order_history, name='order_history'),
]