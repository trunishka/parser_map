
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns

from djgeojson.views import GeoJSONLayerView

from ip_parse.views import home, compromized, subnet
from ip_parse.models import CompromizedIP
from accounts.views import user
from ip_parse import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', home),
    url(r'^accounts/', user, name = "users"),
    url(r'^compromized/', compromized, name="compromized"),
    url(r'^subnet/', subnet, name="subnet"),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name="index"),
    url(r'^info/', views.CompromizedStock.as_view(), name="info"),
    url(r'^data/', GeoJSONLayerView.as_view(model=CompromizedIP, properties=('ip_adress', 'appear_date','geom', 'resourse')), name='data'),

]

# urlpatterns = format_suffix_patterns(urlpatterns)