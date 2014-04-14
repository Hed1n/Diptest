__author__ = 'Хедин'
from django.conf.urls import *
from accounts import views

urlpatterns = patterns('',
    url(r'^registration/$', views.registr),
)
