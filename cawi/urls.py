# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from cawi import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^questionario$', views.questionario, name='questionario'),
                       url(r'^bye$', views.bye, name='bye'),
                       )


