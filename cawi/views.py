# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from cawi import questionario as q
from cawi.models import Questionario

import collections

def convert_key(k):
    if not k.startswith('D'):
        return k

    _k = k.split('-')
    _k1 = _k[0].split('.')
    try:
        if len(_k1[1]) == 1 or (len(_k1[1]) == 2 and _k1[1].endswith('b')):
            _k1[1] = '0'+_k1[1]
            _k[0] = '.'.join(_k1)
    except:
        pass
    return '__'.join(_k).replace('.', '_')

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
        r = ((convert_key(k), v) for k, v in risposte.items())

        risposte1 = collections.OrderedDict(sorted(r))

        q = Questionario(
            id_contatto=idc,
            ip_compilatore=get_client_ip(request),
            risposte=risposte1
        )
        q.save()
    #return render(request, 'bye.html')
    if request.POST.get('idc'):
        return HttpResponseRedirect('/bye?idc=%i' % int(request.POST.get('idc')))

    return HttpResponseRedirect('/bye')
    #return redirect('bye', {'idc': request.POST.get('idc')} )
    #return bye(request, idc = request.POST.get('idc'))

import xlsxwriter
import io

from django.http.response import HttpResponse

from xlsxwriter.workbook import Workbook
from django.utils.encoding import smart_str
import ast
import re

def export(request):
    output = io.BytesIO()

    workbook = xlsxwriter.Workbook(output, {'in_memory': True})
    worksheet = workbook.add_worksheet()

    headers = ['IDQ','IDContatto', 'DataCompilazione', 'IPCompilatore']

    q = Questionario.objects.all()

    if q:
        values = re.search(r"OrderedDict\((.*)\)", q[0].risposte).group(1)
        mydict = collections.OrderedDict(ast.literal_eval(values))

        for c in mydict.keys():
            headers.append(smart_str(c))

    for i, text in enumerate(headers):
        worksheet.write(0, i, text)

    for j, obj in enumerate(q):
        values = re.search(r"OrderedDict\((.*)\)", obj.risposte).group(1)
        mydict = collections.OrderedDict(ast.literal_eval(values))

        row = [
            smart_str(obj.pk),
            smart_str(obj.id_contatto),
            smart_str(obj.data_compilazione.strftime("%d/%m/%Y %H:%M:%S")),
            smart_str(obj.ip_compilatore)
        ]
        for c in mydict.values():
            row.append(smart_str(c))

        for k, text in enumerate(row):
            worksheet.write(j+1, k, text)

    workbook.close()

    output.seek(0)

    response = HttpResponse(output.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response['Content-Disposition'] = "attachment; filename=test.xlsx"

    return response
