from django.urls import path
from accounts.api.views import CreateAccountAPI 
urlpatterns = [
    path('create-account/', CreateAccountAPI.as_view()),
]