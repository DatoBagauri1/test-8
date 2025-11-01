from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Homeeeee'),  
    path('films/', views.films, name='films'),
]
