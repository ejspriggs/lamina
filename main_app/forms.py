from django.contrib.auth.forms import UserCreationForm
from django.forms import CheckboxInput, CharField
from django.contrib.auth.models import User
from .models import Profile


class ExtendedUserCreationForm(UserCreationForm):
    is_northern_hemi = CheckboxInput()
    display_name = CharField(max_length = 100)
    class Meta:
        model = Profile
        fields = ['display_name', 'is_northern_hemi']