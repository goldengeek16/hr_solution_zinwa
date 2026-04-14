
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from dashboard import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Dashboard, name='dashboard'),
    path('employees/', include('employees.urls'), name='employees-list'),
     path('users/', include('users.urls'), name='profiles'),
]
