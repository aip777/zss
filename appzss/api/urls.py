from django.urls import path
from appzss.api.country_views import CountryListAPI, CountryDetailAPIView

urlpatterns = [
    path('country/', CountryListAPI.as_view()),
    path('country/<int:pk>/', CountryDetailAPIView.as_view()),
]