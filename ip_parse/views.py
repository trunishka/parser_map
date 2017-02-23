from django.shortcuts import render
from ip_parse.models import Subnet, CompromizedIP



def compromized(request):

    return render(request, "compromized.html",{"compromized":CompromizedIP.objects.all})

def subnet(request):
    return render(request, "subnet.html")

def index(request):
    return(request, "index.html")

