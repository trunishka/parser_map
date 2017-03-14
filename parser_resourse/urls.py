
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
# from rest_framework.urlpatterns import format_suffix_patterns

from djgeojson.views import GeoJSONLayerView

from ip_parse import serializers
from ip_parse.views import compromized, subnet, test, index
from ip_parse.models import CompromizedIP
from accounts.views import user
from ip_parse import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', user, name = "users"),
    url(r'^compromized/', compromized, name="compromized"),
    url(r'^subnet/', subnet, name="subnet"),
    url(r'^test/', test, name="test"),
    url(r'^$', index, name="index"),
    url(r'^info/', serializers.CompromizedStock.as_view(), name="info"),
    # url(r'^/info/?format=json', name="info1"),
    url(r'^data/', GeoJSONLayerView.as_view(model=CompromizedIP, properties=('ip_adress', 'appear_date', 'malware_type', 'geom', 'resourse')), name='data'),

]

# urlpatterns = format_suffix_patterns(urlpatterns)