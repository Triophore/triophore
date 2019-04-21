from django.shortcuts import render
from . import models
# Create your views here.
from django.core import serializers
from django.http import HttpResponse
from .models import Details


def home(request):
    details_web = Details.objects.all().first()
    context = {
        'details' : details_web,
    }
    return render(request,'website/home/index.html',context)

def page(request,page):
    return render(request,'website/pages/'+page+'.html')

def menu(request):
    menus = models.MenuItem.objects.all()
    print(menus)
    qs_json = serializers.serialize('json', menus)
    context = {
        'menus':menus,
        'json':qs_json
    }
    return render(request,'website/menu.html',context)
