from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import DeleteView
from .forms import ExtendedUserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Fossils, Animal
from django.contrib.auth.decorators import login_required
import requests

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
    if request.method == 'POST':
        checked_items = [i[0] for i in request.POST.items() if i[0] != 'csrfmiddlewaretoken' and i[1] == 'on']
        Animal.objects.filter(type__exact = "bug", name__in = checked_items).delete()
        return redirect('bugs_index')
    else:
        api_url = f'https://api.nookipedia.com/nh/bugs?api_key={api_key}'
        bugs_donated = [f.name for f in request.user.animal_set.filter(type__exact = "bug")]
        bugs = requests.get(api_url).json()
        return render(request, 'animals/config.html', {
            'bugs': bugs,
            'bugs_donated': bugs_donated,
            'animal_type': 'bugs'
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
def bug_got(request, bugs_name):
    if request.method == "POST":
        b, created = Animal.objects.get_or_create(name = bugs_name, type = "bug", weather = "", user = request.user)
        print(f'User {request.user.username} donated bug {b.name}! (New info? {created})')
    return redirect('bugs_index')

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
    if request.method == 'POST':
        checked_items = [i[0] for i in request.POST.items() if i[0] != 'csrfmiddlewaretoken' and i[1] == 'on']
        Animal.objects.filter(type__exact = "fish", name__in = checked_items).delete()
        return redirect('fish_index')
    else:
        api_url = f'https://api.nookipedia.com/nh/fish?api_key={api_key}'
        fish_donated = [f.name for f in request.user.animal_set.filter(type__exact = "fish")]
        fish = requests.get(api_url).json()
        return render(request, 'animals/config.html', {
            'fish': fish,
            'fish_donated': fish_donated,
            'animal_type': 'fish'
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
def fish_got(request, fish_name):
    if request.method == "POST":
        f, created = Animal.objects.get_or_create(name = fish_name, type = "fish", user = request.user)
        print(f'User {request.user.username} donated fish {f.name}! (New info? {created})')
    return redirect('fish_index')

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
    if request.method == 'POST':
        checked_items = [i[0] for i in request.POST.items() if i[0] != 'csrfmiddlewaretoken' and i[1] == 'on']
        Fossils.objects.filter(name__in = checked_items).delete()
        return redirect('fossils_index')
    else:
        api_url = f'https://api.nookipedia.com/nh/fossils/individuals?api_key={api_key}'
        fossils_donated = [f.name for f in request.user.fossils_set.all()]
        fossils = requests.get(api_url).json()
        return render(request, 'fossils/config.html', {
            'fossils': fossils,
            'fossils_donated': fossils_donated
        })

@login_required
def fossil_details(request, fossil_name):
    api_url = f'https://api.nookipedia.com/nh/fossils/individuals/{fossil_name}?api_key={api_key}'
    fossil = requests.get(api_url).json()
    return render(request, 'fossils/fossil_details.html', {
        'fossil': fossil
    })

@login_required
def fossil_got(request, fossil_name):
    if request.method == "POST":
        f, created = Fossils.objects.get_or_create(name = fossil_name, user = request.user)
        print(f'User {request.user.username} donated fossil {f.name}! (New info? {created})')
    return redirect('fossils_index')

@login_required
def choose_collectible(request):
    collectibles = {
        'fish_left': 80 - request.user.animal_set.filter(type__exact = "fish").count(),
        'bugs_left': 80 - request.user.animal_set.filter(type__exact = "bug").count(),
        'fossils_left': 73 - request.user.fossils_set.count()
    }
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


class AnimalDelete(DeleteView):
    model = Animal
    success_url = '/bugs'

class FossilDelete(DeleteView):
    model = Fossils
    sucess_url = '/fossils'