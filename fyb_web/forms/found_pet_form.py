from django import forms
from fyb_web.models import FoundPet


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