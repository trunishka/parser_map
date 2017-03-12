from django.shortcuts import render
from ip_parse.models import Subnet, CompromizedIP

from ip_parse.forms import  ProductFilter



def compromized(request):

    return render(request, "compromized.html",{"compromized":CompromizedIP.objects.all})

def subnet(request):
    return render(request, "subnet.html")

def index(request):
    return(request, "index.html")

def product_list(request):
    filter = ProductFilter(request.GET, queryset=CompromizedIP.objects.all())
    return render(request, 'my_app/template.html', {'filter': filter})

def info(request):
    return(request, ".html")

def test(request):
    sample = CompromizedIP.objects.all()
    number = []
    for one in sample:
        number.append([one.appear_date, one.ip_adress, one.as_number, one.malware_type,one.resourse, one.lat, one.long])
    return render(request, "test.html", {"number": number})