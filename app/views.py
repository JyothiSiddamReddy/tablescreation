from django.shortcuts import render

# Create your views here.
from app.models import *

def country(request):
    CTO=Country.objects.all()
   
    d={'country':CTO}
    return render(request,'country.html',d)




def capital(request):
     CO=Capital.objects.all()
     d={'capital':CO}
     return render(request,'capital.html',d)
