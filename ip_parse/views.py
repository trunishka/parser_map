from django.shortcuts import render
from ip_parse.models import Subnet, CompromizedIP
from ip_parse.forms import TestForm

def compromized(request):
    return render(request, "compromized.html",{"compromized":CompromizedIP.objects.all})

def subnet(request):
    return render(request, "subnet.html")

def index(request):
    return(request, "index.html")


def test(request):
    form = TestForm(request.POST)

    number = []
    if request.method == 'POST':
        malware = request.POST.get('malware')
        resourse = None if request.POST.get('resourse') == '' else request.POST.get('resourse')

        filter_params = {}

        if resourse != None:
            filter_params.update({
                'resourse' : resourse
            })
        if resourse != None:
            filter_params.update({
                'resourse' : resourse
            })

        sample = CompromizedIP.objects.filter(**filter_params)
        print(sample, malware, resourse)
        for one in sample:
           number.append([one.appear_date, one.ip_adress, one.as_number, one.malware_type, one.resourse, one.lat, one.long])
    else:
        sample = CompromizedIP.objects.all()
        for one in sample:
            number.append([one.appear_date, one.ip_adress, one.as_number, one.malware_type, one.resourse, one.lat, one.long])
    return render(request, "test.html", {"number": number, 'form':form})