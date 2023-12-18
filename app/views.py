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




def insert_country(request):
     cid=int(input('Enter the id: '))
     cname=input('Enter the name: ')

     CO=Country.objects.get_or_create(country_Id=cid,country_Name=cname)[0]
     CO.save()
     CTO=Country.objects.all()
     d={'country':CTO}
     return render(request,'country.html',d)



def insert_capital(request):
     id=int(input('Enter the id: '))
     cname=input('Enter the name: ')
     cid=int(input('Enter the id: '))
     co=Country.objects.get(country_Id=cid)

     CO=Capital.objects.get_or_create(capital_Id=id,capital_Name=cname,country_Id=co)[0]
     CO.save()
     CTO=Capital.objects.all()
     d={'capital':CTO}
     return render(request,'capital.html',d)
