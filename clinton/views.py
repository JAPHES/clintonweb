from django.shortcuts import render
from django.http import FileResponse
import os
from django.conf import settings

def download_cv(request):
    filepath = os.path.join(settings.BASE_DIR, 'clinton/static/clinton/files/clintoncv.pdf')
    return FileResponse(open(filepath, 'rb'), as_attachment=True, filename='clintoncv.pdf')


# Create your views here.
def home(request):
    return render(request, 'home.html')

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    return render(request, 'contact.html')