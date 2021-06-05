from django.db import models
from django_countries.fields import CountryField    
import pytz

# Create your models here.


class Country(models.Model):
    country_code = {}
    choice_country = []
    for key, val in pytz.country_names.items():
        obj = {val:key}
        country_code.update(obj)
        choice_country.append((val,val))
    country_name = tuple(choice_country)

    name = models.CharField(max_length=50, choices=country_name)
    latitude = models.FloatField(max_length=150, blank=False)
    longitude = models.FloatField(max_length=150, blank=False)
    code = models.CharField(max_length=5, blank=True)


    def save(self, *args, **kwargs):
        if self.name in self.country_code:
            self.code = self.country_code[self.name]
        super(Country, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Country'

class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'State'
        verbose_name_plural = 'State'

class Address(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False)
    house_number = models.CharField(max_length=100, blank=False)
    road_number = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Address'