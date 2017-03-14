from ip_parse.models import CompromizedIP
from django import forms


class TestForm(forms.Form):
    malware = forms.CharField(label = "malware", max_length= 100, required=False)
    resourse = forms.CharField(label = "resourse", max_length=100, required=False)