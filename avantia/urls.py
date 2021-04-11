from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    #apps
    path('',include('users.urls', namespace='users')),
    path('api/',include('users.endpoints_urls', namespace='api_users')),
]
