
from django.contrib import admin
# from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # path('api/login/',obtain_auth_token),
    path('api/', include('pharmacy.urls')),
    path('accounts/', include('accounts.urls')),
]
