# -*- coding: utf-8 -*-
from django.contrib import admin
from cawi.models import Questionario

from django.http import HttpResponse
import collections

def export_csv(modeladmin, request, queryset):
    import csv
    import datetime
    from django.utils.encoding import smart_str
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=cawi_export-%s.csv' % datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)

    #cols = queryset[0].risposte
    cols = [
        smart_str(u"ID"),
        smart_str(u"id_contatto"),
        smart_str(u"data_ora"),
        smart_str(u"ip_compilatore"),
    ]
    import ast
    import re
    values = re.search(r"OrderedDict\((.*)\)", queryset[0].risposte).group(1)
    mydict = collections.OrderedDict(ast.literal_eval(values))

    for c in mydict.keys():
        cols.append(smart_str(c))

    #print(queryset[0].risposte)
    # writer.writerow([
    #     smart_str(u"ID"),
    #     smart_str(u"id_contatto"),
    #     smart_str(u"data_ora"),
    #     ])
    writer.writerow(cols)
    for obj in queryset:
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

        writer.writerow(row)
    return response
export_csv.short_description = u"Export CSV"

# Register your models here.
class QuestionarioAdmin(admin.ModelAdmin):
    #fields = ['id_contatto', 'data_compilazione', 'ip_compilatore', 'risposte']
    list_display = ('id_contatto', 'data_compilazione', 'ip_compilatore')
    actions = [export_csv, ]

admin.site.register(Questionario, QuestionarioAdmin)
