from django.urls import path
from punti import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]