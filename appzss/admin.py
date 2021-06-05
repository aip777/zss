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

admin.site.register(State)
admin.site.register(Address)