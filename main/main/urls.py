
from django.contrib import admin
# from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from django.urls.conf import include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('pharmacy.urls')),
    path('accounts/', include('accounts.urls')),
]
