from django.urls import path
from appzss.view.country import (
    addCountryView, 
    countrylistView, 
    updateCountryView, 
    deleteCountryView,
    )
from appzss.view.state import (
    addStateView,
    statelistView,
    updateStateView,
    deleteStateView
    )

from appzss.view.address import (
    addAddressView,
    addressListView,
    updateAddressView,
    deleteAddressView
    )

urlpatterns = [
    path('add-country/', addCountryView, name='add-country'),
    path('', countrylistView, name='country-list'),
    path('update-country/<int:id>/', updateCountryView, name='update-country'),
    path('delete-country/<int:id>/', deleteCountryView, name='country-delete'),

    path('add-state/', addStateView, name='add-state'),
    path('state-list/', statelistView, name='state-list'),
    path('update-state/<int:id>/', updateStateView, name='update-state'),
    path('delete-state/<int:id>/', deleteStateView, name='state-delete'),

    path('add-address/', addAddressView, name='add-address'),
    path('address-list/', addressListView, name='address-list'),
    path('update-address/<int:id>/', updateAddressView, name='update-address'),
    path('delete-address/<int:id>/', deleteAddressView, name='address-delete'),
]
