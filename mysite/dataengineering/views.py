from django.http import HttpResponse, Http404
import os
from datetime import datetime
from django.template import loader
from django.shortcuts import render

def getBreadCrumbData(request):
    courseStartDate = datetime(2021, 1, 11)  # (yyyy-m-d) date on which first file is served
    today = datetime.today()
    if today < courseStartDate:
        return HttpResponse('<h1>Course has not yet begun.</h1>')
    file_number = (today - courseStartDate).days + 2
    filename = 'day%s' % file_number + '.json'
    file_path = os.path.join('dataengineering', 'static', 'dataengineering', filename)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read())
            response['Content-Type'] = 'application/json'
            # https://code.djangoproject.com/ticket/31091 (for connection drops)
            # response['Connection'] = 'close'
            response['Content-Disposition'] = 'attachment; filename=%s'%(datetime.today().strftime('%Y-%m-%d'))+'.json'
            return response
    raise Http404

def getCadData(request):
    courseStartDate = datetime(2021, 1, 11)  # (yyyy-m-d) date on which first file is served
    today = datetime.today()
    if today < courseStartDate:
        return HttpResponse('<h1>Course has not yet begun.</h1>')
    file_number = (today - courseStartDate).days + 7
    filename = 'cad_table_day_%s' % file_number + '.html'
    file_path = os.path.join('dataengineering', 'templates', filename) # may be filepath?
    if os.path.exists(file_path):
        return render(request, filename)
    raise Http404

