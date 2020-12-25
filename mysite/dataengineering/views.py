from django.http import HttpResponse, FileResponse, Http404, StreamingHttpResponse
import os
from datetime import datetime


def index(request):
    courseStartDate = datetime(2020, 12, 24)  # date on which first file is served
    file_number = (datetime.today() - courseStartDate).days + 2
    filename = 'day%s' % file_number + '.json'
    file_path = os.path.join('dataengineering', 'static', 'dataengineering', filename)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read())
            response['Content-Type'] = 'application/json'
            response['Content-Disposition'] = 'attachment; filename=%s' % (datetime.today().strftime('%Y-%m-%d'))+'.json'
            return response
    raise Http404