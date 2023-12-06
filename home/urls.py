from django.contrib import admin
from django.urls import path
from home import views

# HTTP Request <-> HTTP Response
# MVT (MVC)
app_name = 'home'

urlpatterns = [
    path('', views.home, name='index'),
]
