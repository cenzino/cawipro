# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from cawi import questionario as q

def index(request):
    qu = { 'q': q.questionario }
    return render(request, 'index.html', qu)

def questionario(request):
    qu = { 'q': q.questionario }
    return render(request, 'questionario.html', qu )

def bye(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'bye.html')
