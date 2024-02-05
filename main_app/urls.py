from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('animals/', views.animals_index, name='animals_index'),
    path('fossils/', views.fossils_index, name='fossils_index'),
]