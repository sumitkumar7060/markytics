from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.index, name='hello'),
    path('register', views.register, name='register'),
    path('registration', views.Registration, name='registration'),
    path('login', views.login, name='login'),
    path('log_in', views.log_in, name='log_in'),
    path('logout/', views.logout, name='logout'),
    path('incident', views.Incident, name='incident'),
    path('incidents', views.inc, name='inc')
]
