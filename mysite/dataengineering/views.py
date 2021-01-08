from django.http import HttpResponse, FileResponse, Http404, StreamingHttpResponse
import os
from datetime import datetime
from django.utils import timezone

def index(request):
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
            response['Content-Disposition'] = 'attachment; filename=%s'%(datetime.today().strftime('%Y-%m-%d'))+'.json'
            return response
    raise Http404
