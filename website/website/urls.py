
from django.contrib import admin
from django.urls import path, include
#from TechCourses import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('TechCourses.urls')),
    #path('<int:course_id>/', views.detail, name='detail'),

]
