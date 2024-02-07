from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import ExtendedUserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Fossils, Animal
from django.contrib.auth.decorators import login_required
import requests

# Mock data for initial design
animals = [
    {'name': 'Anchovy', 'type': 'Fish', 'image': 'https://dodo.ac/np/images/7/7f/Anchovy_%28Fish%29_NH_Icon.png', 'time_of_year': 'All Year', 'south_hemi_toy': 'All Year', 'location': 'Sea', 'shadow_size': 'Small', 'Weather': '', 'value': 200, 'misc': 'I caught an anchovy! Stay away from my pizza!'},
    {'name': 'Football Fish', 'type': 'Fish', 'image': 'https://dodo.ac/np/images/3/34/Football_Fish_NH_Icon.png', 'time_of_year': 'Nov - Mar', 'south_hemi_toy': 'May - Sep', 'location': 'Sea', 'shadow_size': 'Large', 'Weather': '', 'value': 2500, 'misc': 'I caught a football fish! Some countries call it a soccer fish!'},
    {'name': 'Atlas Moth', 'type': 'Bug', 'image': 'https://dodo.ac/np/images/7/7f/Atlas_Moth_NH_Icon.png', 'time_of_year': 'Apr - Sep', 'south_hemi_toy': 'Oct - Mar', 'location': 'On trees (any kind)', 'shadow_size': '', 'Weather': '', 'value': 3000, 'misc': 'I caught an Atlas moth! I bet it never gets lost!'},
    {'name': 'Bell Cricket', 'type': 'Bug', 'image': 'https://dodo.ac/np/images/4/4a/Bell_Cricket_NH_Icon.png', 'time_of_year': 'Sep - Oct', 'south_hemi_toy': 'Mar - Apr', 'location': 'On the ground', 'shadow_size': '', 'weather': '', 'value': 430, 'misc': 'I caught a bell cricket! It would make a great bellhop!'},
]

fossils = [
    {'name': 'Amber', 'image': 'https://dodo.ac/np/images/7/7f/Amber_NH_Icon.png', 'value': 1200},
    {'name': 'Ankylo Skull', 'image': 'https://dodo.ac/np/images/4/45/Ankylo_Skull_NH_Icon.png', 'value': 3500},
]

collectibles = {
    'fish_left': 7,
    'bugs_left': 21,
    'fossils_left': 16
}

api_key = '843450ff-ae8c-4884-83b6-6153eb441bd0'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def bugs_index(request):
    api_url = f'https://api.nookipedia.com/nh/bugs?api_key={api_key}'
    bugs_donated = [f.name for f in request.user.animal_set.filter(type__exact = "bug")]
    bugs = [b for b in requests.get(api_url).json() if b["name"] not in bugs_donated]
    return render(request, 'animals/index.html', {
        'bugs': bugs,
        'animal_type': 'bugs'
    })

@login_required
def bugs_config(request):
    api_url = f'https://api.nookipedia.com/nh/bugs?api_key={api_key}'
    bugs_donated = [f.name for f in request.user.animal_set.filter(type__exact = "bug")]
    bugs = requests.get(api_url).json()
    return render(request, 'animals/config.html', {
        'bugs': bugs,
        'bugs_donated': bugs_donated,
        'animal_type': 'bugs'
    })

@login_required
def fish_index(request):
    api_url = f'https://api.nookipedia.com/nh/fish?api_key={api_key}'
    fish_donated = [f.name for f in request.user.animal_set.filter(type__exact = "fish")]
    fish = [f for f in requests.get(api_url).json() if f["name"] not in fish_donated]
    return render(request, 'animals/index.html', {
        'fish': fish,
        'animal_type': 'fish'
    })

@login_required
def fish_config(request):
    api_url = f'https://api.nookipedia.com/nh/fish?api_key={api_key}'
    fish_donated = [f.name for f in request.user.animal_set.filter(type__exact = "fish")]
    fish = requests.get(api_url).json()
    return render(request, 'animals/index.html', {
        'fish': fish,
        'fish_donated': fish_donated,
        'animal_type': 'fish'
    })

@login_required
def fossils_index(request):
    api_url = f'https://api.nookipedia.com/nh/fossils/individuals?api_key={api_key}'
    fossils_donated = [f.name for f in request.user.fossils_set.all()]
    fossils = [f for f in requests.get(api_url).json() if f["name"] not in fossils_donated]
    return render(request, 'fossils/index.html', {
        'fossils': fossils
    })

@login_required
def fossils_config(request):
    api_url = f'https://api.nookipedia.com/nh/fossils/individuals?api_key={api_key}'
    fossils_donated = [f.name for f in request.user.fossils_set.all()]
    fossils = requests.get(api_url).json()
    return render(request, 'fossils/index.html', {
        'fossils': fossils,
        'fossils_donated': fossils
    })

@login_required
def bug_details(request, bugs_name):
    api_url = f'https://api.nookipedia.com/nh/bugs/{bugs_name}?api_key={api_key}'
    bug = requests.get(api_url).json()
    return render(request, 'animals/animal_details.html', {
        'bug': bug,
        'animal_type': 'bugs'
    })

@login_required
def fish_details(request, fish_name):
    api_url = f'https://api.nookipedia.com/nh/fish/{fish_name}?api_key={api_key}'
    fish = requests.get(api_url).json()
    return render(request, 'animals/animal_details.html', {
        'fish': fish,
        'animal_type': 'fish'
    })
@login_required
def fossil_details(request, fossil_name):
    api_url = f'https://api.nookipedia.com/nh/fossils/individuals/{fossil_name}?api_key={api_key}'
    fossil = requests.get(api_url).json()
    return render(request, 'fossils/fossil_details.html', {
        'fossil': fossil
    })

@login_required
def choose_collectible(request):
    return render(request, 'choose_collectible.html', collectibles)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('choose_collectible')
        else:
            error_message = 'Invalid sign-up, please try again.'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

def signup2(request):
    error_message = ''
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            display_name = form.cleaned_data.get('display_name')
            is_northern_hemi = form.cleaned_data.get('is_northern_hemi')
            user = User.objects.get(username = username)
            profile = Profile.objects.create(user = user, display_name = display_name, is_northern_hemi = is_northern_hemi)
            profile.save()
            login(request, user)
            return redirect('choose_collectible')
        else:
            error_message = 'Invalid sign-up, please try again.'
    form = ExtendedUserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
