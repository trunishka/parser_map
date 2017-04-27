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
    form = TestForm()
    sample = CompromizedIP.objects.all()
    if request.method == 'POST':
        form = TestForm(request.POST)
#         malware = None if request.POST.get('malware') == '' else request.POST.get('malware')
#         resourse = None if request.POST.get('resourse') == '' else request.POST.get('resourse')
#         print("asdf", form)

        if form.is_valid():
            filter_params = {}
            if form.cleaned_data.get("resourse"):
                print(resourse)
                filter_params.update({
                    'resourse' : resourse
                })
            if form.cleaned_data.get("malware"):
                filter_params.update({
                    'malware_type' : malware
                })
        sample = sample.filter(**filter_params)
    for one in sample:
        number.append([one.appear_date.isoformat(), one.ip_adress, one.as_number, one.malware_type, one.resourse, one.lat, one.long])
    return render(request, "test.html", {"number": number, 'form':form})
