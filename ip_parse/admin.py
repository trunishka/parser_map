from django.contrib import admin
from ip_parse.models import Subnet, Compromized_IP


admin.site.register(Subnet)
admin.site.register(Compromized_IP)
