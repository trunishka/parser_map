from django.db import models
from djgeojson.fields import PointField



class Subnet(models.Model):
    as_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    range_of_ip = models.CharField(max_length=20)

    def __str__(self):
        return self.as_number


class CompromizedIP(models.Model):
    title = models.CharField(max_length=255, default='', unique=True)
    appear_date = models.DateField(auto_now=False, auto_now_add=False)
    ip_adress = models.CharField(max_length = 15)
    as_number = models.CharField(Subnet, max_length=15, blank=True, null=True)
    malware_type = models.CharField(max_length=255)
    resourse = models.CharField(max_length=2555)
    long = models.FloatField()
    lat = models.FloatField()

    # first_create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    # last_update_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.title
