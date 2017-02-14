from django.shortcuts import render
from ip_parse.models import Subnet, Compromized_IP
from rest_framework.views import APIView
from rest_framework.response import Response
from ip_parse.serializers import CompromizedSerializer


def home(request):
    sub = Subnet.objects.get(pk = 1)
    name="Vasya"
    return render(request, "home.html", {"sub":sub})

def compromized(request):

    return render(request, "compromized.html",{"compromized":Compromized_IP.objects.all})

def subnet(request):
    return(request, "subnet.html")

def index(request):

    return(request, "index.html")

class CompromizedStock(APIView):

    def get(self, request):
        compromized = Compromized_IP.objects.all()
        serialazer = CompromizedSerializer(compromized, many = True)
        return Response(serialazer.data)