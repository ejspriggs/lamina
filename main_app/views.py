from django.shortcuts import render

# Create your views here.
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

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# Current view to see all the bugs and fishes
def animals_index(request):
    return render(request, 'animals/index.html', {
        'animals': animals
    })

# Current view to see all the fossils
def fossils_index(request):
    return render(request, 'fossils/index.html', {
        'fossils': fossils
    })