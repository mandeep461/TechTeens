from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('about', views.about, name ='AboutUs'),
    path('contact', views.contact, name ='ContactUs'),
    path('python', views.python, name = 'Python'),
    path('machinelearning', views.ml, name = 'MachineLeaning'),
    path('django', views.dj, name = 'Django'),
    path('datascience', views.ds, name = 'DataScience')
]