# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from cawi import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^questionario$', views.questionario, name='questionario'),
                       url(r'^salva_questionario$', views.salva_questionario, name='salva_questionario'),
                       url(r'^bye$', views.bye, name='bye'),
                       url(r'^export$', views.export, name='export'),
                       url(r'^ateco$', views.ateco, name='ateco'),
                       )


