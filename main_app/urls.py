from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('bugs/', views.bugs_index, name='bugs_index'),
    path('bugs/<bugs_name>/', views.bug_details, name='bug_details'),
    path('bugs/<bugs_name>/gotit/', views.bug_got, name='bug_got'),
    path('fish/', views.fish_index, name='fish_index'),
    path('fish/<fish_name>/', views.fish_details, name='fish_details'),
    path('fish/<fish_name>/gotit/', views.fish_got, name='fish_got'),
    path('fossils/', views.fossils_index, name='fossils_index'),
    path('fossils/<fossil_name>/', views.fossil_details, name='fossil_details'),
    path('fossils/<fossil_name>/gotit/', views.fossil_got, name='fossil_got'),
    path('collectibles/', views.choose_collectible, name='choose_collectible'),
    path('accounts/signup/', views.signup, name='signup')
]