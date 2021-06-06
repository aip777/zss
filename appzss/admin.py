from django.contrib import admin
from .models import Country, State, Address
# Register your models here.
import pytz

class CountryAdmin(admin.ModelAdmin):
  list_display = (
    'id',
    'name',
    'latitude',
    'longitude',
    'code',
  )
  list_display_links = ('id', 'name')
  search_fields = ['id','name', 'latitude','longitude','code']
  list_per_page = 15
  readonly_fields=('code',)

admin.site.register(Country, CountryAdmin)


class StateAdmin(admin.ModelAdmin):
  list_display = (
    'id',
    'name',
    'country',
  )
  list_display_links = ('id', 'name')
  list_per_page = 15

admin.site.register(State, StateAdmin)

class AddressAdmin(admin.ModelAdmin):
  list_display = (
    'id',
    'name',
    'state',
  )
  list_display_links = ('id', 'name')
  list_per_page = 15
admin.site.register(Address, AddressAdmin)