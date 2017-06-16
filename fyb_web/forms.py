from django.contrib.auth.models import User
from django import forms

from website.models import LostPet
from website.models import FoundPet


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name',)


class LostPetForm(forms.ModelForm):

    class Meta:
        model = LostPet
        fields = (
            'name',
            'species',
            'breed',
            'description',
            'last_seen_location',
            'reward',
        )


class FoundPetForm(forms.ModelForm):

    class Meta:
        model = FoundPet
        fields = (
            'name',
            'species',
            'breed',
            'description',
            'last_seen_location',
        )