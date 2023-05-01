from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def botcatcher(request):
    SO=StudentForm()
    d={'SO':SO}
    if request.method=='POST':
        SWD=StudentForm(request.POST)
        if SWD.is_valid():
            return HttpResponse('Correct')
        else:
            return HttpResponse('Wrong')
    return render(request,'botcatecher.html',d)