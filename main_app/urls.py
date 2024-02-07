from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('bugs/', views.bugs_index, name='bugs_index'),
    path('fish/', views.fish_index, name='fish_index'),
    path('fossils/', views.fossils_index, name='fossils_index'),
    path('collectibles/', views.choose_collectible, name='choose_collectible'),
    path('accounts/signup/', views.signup, name='signup'),
    path('bugs/<bugs_name>/', views.bug_details, name='animal_details'),
    path('fish/<fish_name>/', views.fish_details, name='animal_details'),
    path('fossils/<fossil_name>/', views.fossil_details, name='fossil_details')
]