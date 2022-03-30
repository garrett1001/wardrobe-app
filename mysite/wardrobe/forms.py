from django import forms
from .models import Garment, Outfit
  
class GarmentForm(forms.ModelForm):
    class Meta:
        model = Garment
        fields = ['name', 'image', 'category', 'description']

class OutfitForm(forms.ModelForm):
    garments = forms.ModelMultipleChoiceField(
        queryset=Garment.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True)

    class Meta:
        model = Outfit
        fields = ['name', 'image', 'description', 'garments']

    def __init__(self, *args, **kwargs):
        current_user = kwargs.pop('user')
        super(OutfitForm, self).__init__(*args, **kwargs)
        self.fields['garments'].queryset = Garment.objects.filter(user=current_user)