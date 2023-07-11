from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *

def sf(request):
    SFO=studentform()
    d={'SFO':SFO}
    if request.method =='POST':
        SFD=studentform(request.POST)
        if SFD.is_valid():
            return HttpResponse('is_valid')
        else:
            return HttpResponse('in_valid data')
    return render(request,'sf.html',d)