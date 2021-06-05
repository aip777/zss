from django.urls import path
from appzss.api.country_views import CountryListAPI, CountryDetailAPIView
from appzss.api.state_view import StateListAPI, StateDetailAPIView

urlpatterns = [
    path('country/', CountryListAPI.as_view()),
    path('country/<int:pk>/', CountryDetailAPIView.as_view()),

    path('state/', StateListAPI.as_view()),
    path('state/<int:pk>/', StateDetailAPIView.as_view()),
 
]