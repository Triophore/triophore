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
    try:
        print(page)
        if page == "products":
            content = request.GET['content']
            return render(request,'website/pages/products/'+content+'.html')
        if page == "services":
            content = request.GET['content']
            return render(request,'website/pages/services/'+content+'.html')
        if page == "wiki":
            category = request.GET['category']
            subcategory = request.GET['subcategory']
            return render(request,'website/wiki/index.html')
        if page == "news":
            content = request.GET['content']
            return render(request,'website/news/'+content+'.html')
        else:
            return render(request,'website/pages/'+page+'.html')
    except:
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
