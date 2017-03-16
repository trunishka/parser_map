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
    number = []
    form = TestForm(request.POST)
    if request.method == 'POST':
        malware = None if request.POST.get('malware') == '' else request.POST.get('malware')
        resourse = None if request.POST.get('resourse') == '' else request.POST.get('resourse')
        filter_params = {}
        print("asdf", form)
        if form.is_valid():
            if resourse != None:
                print(resourse)
                filter_params.update({
                    'resourse' : tuple(resourse)
                })
            if malware != None:
                filter_params.update({
                    'malware_type' : malware
                })
            sample = CompromizedIP.objects.filter(**filter_params)
            print(sample, malware, resourse)
        for one in sample:
           number.append([one.appear_date.isoformat(), one.ip_adress, one.as_number, one.malware_type, one.resourse, one.lat, one.long])
    else:
        sample = CompromizedIP.objects.all()
        for one in sample:
            number.append([one.appear_date.isoformat(), one.ip_adress, one.as_number, one.malware_type, one.resourse, one.lat, one.long])
    return render(request, "test.html", {"number": number, 'form':form})