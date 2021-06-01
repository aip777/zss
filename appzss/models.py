from django.db import models
from django_countries.fields import CountryField    
import pytz

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=2, choices=pytz.country_names.items())
    latitude = models.FloatField(max_length=150, blank=False)
    longitude = models.FloatField(max_length=150, blank=False)
    code = models.CharField(max_length=5, blank=True)


    def save(self, *args, **kwargs):
        self.code = self.name
        super(Country, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name

