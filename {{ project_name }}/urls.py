from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('web_views.urls')),
    path('admin/', admin.site.urls),
]
