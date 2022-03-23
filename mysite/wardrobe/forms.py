from django import forms
from .models import Garment, Outfit
  
class GarmentForm(forms.ModelForm):
    class Meta:
        model = Garment
        fields = ['name', 'image', 'category', 'description']

class OutfitForm(forms.ModelForm):
    class Meta:
        model = Outfit
        fields = ['name', 'image', 'description', 'garments']

        # garments = forms.ModelMultipleChoiceField(
        #     queryset=Garment.objects.all(),
        #     widget=forms.CheckboxSelectMultiple
        # )