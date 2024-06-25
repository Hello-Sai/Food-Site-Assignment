from django.shortcuts import render
# Create your views here.
from .models import *
def home(request):
    search_item =  request.GET.get('search')
    rests = []
    if search_item:
        restaurants = Restaurant.objects.filter(items__icontains=search_item)
        for r in restaurants:
            name = r.name
            items =[i for i in  r.items.keys() if search_item.lower() in i.lower()]
            rests.append([name,items])
    else:
        restaurants = Restaurant.objects.all()
        for r in restaurants:
            name = r.name
            items =[i for i in  r.items.keys()]
            rests.append([name,items])
    return render(request,'index.html',{'restaurants':rests})