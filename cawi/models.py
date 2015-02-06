# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Ateco(models.Model):
    codice = models.CharField(max_length=10)
    descrizione = models.CharField(max_length=255)
    fulltext = models.CharField(max_length=255)

class Questionario(models.Model):
    id_contatto = models.IntegerField()
    data_compilazione = models.DateTimeField(auto_now_add=True, editable=False)
    ip_compilatore = models.CharField(max_length=20, editable=False, default='127.0.0.1')
    risposte = models.TextField()
