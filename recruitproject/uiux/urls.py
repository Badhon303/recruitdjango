from django.urls import path
from uiux import views

urlpatterns = [
    path('', views.uiux, name='index'),   
]