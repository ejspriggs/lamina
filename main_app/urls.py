from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('bugs/', views.bugs_index, name='bugs_index'),
    path('bugs/<bugs_name>/details/', views.bug_details, name='bug_details'),
    path('bugs/<bugs_name>/gotit/', views.bug_got, name='bug_got'),
    path('bugs/configuration/', views.bugs_config, name='bugs_config'),
    path('fish/', views.fish_index, name='fish_index'),
    path('fish/<fish_name>/details/', views.fish_details, name='fish_details'),
    path('fish/<fish_name>/gotit/', views.fish_got, name='fish_got'),
    path('fish/configuration/', views.fish_config, name='fish_config'),
    path('fossils/', views.fossils_index, name='fossils_index'),
    path('fossils/<fossil_name>/details/', views.fossil_details, name='fossil_details'),
    path('fossils/<fossil_name>/gotit/', views.fossil_got, name='fossil_got'),
    path('fossils/configuration', views.fossils_config, name='fossils_config'),
    path('collectibles/', views.choose_collectible, name='choose_collectible'),
    path('accounts/signup/', views.signup, name='signup'),
    path('404', views.test404, name='404')
]