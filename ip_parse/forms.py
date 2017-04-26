from ip_parse.models import CompromizedIP
from django import forms


objects= CompromizedIP.objects.all()
malwarelist = [(None, "-----")]
resourselist = [(None, "-----")]


for element in objects:
    resourseobject = element.resourse
    titleobject = element.title
    appeardateobject = element.appear_date
    ipadressobject = element.ip_adress
    malwareobject = element.malware_type

    malwarelist.append((malwareobject, malwareobject))
    resourselist.append((resourseobject,resourseobject))


class TestForm(forms.Form):
    malware = forms.ChoiceField(label = "malware",  initial=" ", widget=forms.Select(), choices=set(malwarelist), required=False)
    resourse = forms.ChoiceField(label = "resourse",  initial=" ", choices=set(resourselist), widget=forms.Select(), required=False)

