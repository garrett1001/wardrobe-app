from django import forms
from django.utils.safestring import mark_safe
from .models import Garment, Outfit
  
class GarmentForm(forms.ModelForm):
    class Meta:
        model = Garment
        fields = ['name', 'image', 'category', 'description']

class CustomMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return mark_safe("<div class='card'><img src='%s' class='card-img-top' alt='garment'><div class='card-body'><p class='card-text'>%s</p></div></div>"
                            % (obj.image.url, obj.name))

class OutfitForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(OutfitForm, self).__init__(*args, **kwargs)
        self.fields['garments'].queryset = Garment.objects.filter(user=self.request.user).order_by('-category')
    
    class Meta:
        model = Outfit
        fields = ['name', 'image', 'description', 'garments']

    garments = CustomMultipleChoiceField(
        queryset=None,
        widget=forms.CheckboxSelectMultiple,
        required=True)