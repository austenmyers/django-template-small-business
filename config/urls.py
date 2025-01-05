from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('project_apps.home.urls')),
    path('admin/', admin.site.urls),
]
