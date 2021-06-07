from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('appzss.api.urls')),
    path('', include('appzss.urls')),
    path('', include('accounts.urls')),
    path('account/', include('accounts.api.urls')),
]
