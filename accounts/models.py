from django.contrib.auth.models import AbstractUser
from django.db import models


class User(models.Model):
    birthday = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=255, default="Ukraine")


    def __str__(self):
        return (self.country)

    def get_upper_email(self):
        return self.email.upper()


class Test(models.Model):
    iq = models.CharField(max_length=255)

    def __str__ (self):
        return(self.iq)