from django import forms
from fyb_web.models import LostPet


class LostPetForm(forms.ModelForm):

    class Meta:
        model = LostPet
        fields = (
            'name',
            'species',
            'breed',
            'description',
            'contact_info',
        )