
from django.contrib import admin
from django.urls import path, include
from ytube import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ytube, name='youtube'),
]
