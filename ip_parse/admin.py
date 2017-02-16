from django.contrib import admin
from ip_parse.models import Subnet, CompromizedIP


admin.site.register(Subnet)
admin.site.register(CompromizedIP)
