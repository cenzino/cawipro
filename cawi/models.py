# -*- coding: utf-8 -*-
from django.db import models

class Questionario(models.Model):
    id_contatto = models.IntegerField()
    data_compilazione = models.DateTimeField(auto_now_add=True, editable=False)
    ip_compilatore = models.CharField(max_length=20, editable=False, default='0.0.0.0')
    risposte = models.TextField()
