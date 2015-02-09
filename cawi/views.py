# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from cawi import questionario as q
from cawi.models import Questionario

import collections

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def index(request, idc=None):
    idc = request.GET.get('idc')

    print(get_client_ip(request))
    qu = { 'q': q.questionario, 'idc': idc }
    return render(request, 'index.html', qu)

def questionario(request, idc=None):
    idc = request.GET.get('idc')
    qu = { 'q': q.questionario, 'idc': idc }
    return render(request, 'questionario.html', qu )

def bye(request, idc=None):
    idc = request.GET.get('idc')
    return render(request, 'bye.html', { 'idc': idc })


def salva_questionario(request):
    if request.method == 'POST':
        idc = request.POST.get('idc')
        print(idc)
        if idc is None:
            idc = -1
        #request.POST.pop('csrfmiddlewaretoken')
        #d = dict(request.POST .iterlists())
        risposte = collections.OrderedDict(sorted(request.POST.dict().items()))
        q = Questionario(
            id_contatto=idc,
            ip_compilatore=get_client_ip(request),
            risposte=risposte
        )
        q.save()
    #return render(request, 'bye.html')
    if request.POST.get('idc'):
        return HttpResponseRedirect('/bye?idc=%i' % int(request.POST.get('idc')))

    return HttpResponseRedirect('/bye')
    #return redirect('bye', {'idc': request.POST.get('idc')} )
    #return bye(request, idc = request.POST.get('idc'))