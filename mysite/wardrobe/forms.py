from django import forms
from django.utils.safestring import mark_safe
from .models import Outfit, Top, Bottom, Outerwear, Footwear, Accessory
  
class TopForm(forms.ModelForm):
    class Meta:
        model = Top
        fields = ['name', 'image', 'description']

class BottomForm(forms.ModelForm):
    class Meta:
        model = Bottom
        fields = ['name', 'image', 'description']

class OuterwearForm(forms.ModelForm):
    class Meta:
        model = Outerwear
        fields = ['name', 'image', 'description']

class FootwearForm(forms.ModelForm):
    class Meta:
        model = Footwear
        fields = ['name', 'image', 'description']

class AccessoryForm(forms.ModelForm):
    class Meta:
        model = Accessory
        fields = ['name', 'image', 'description']

class CustomMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return mark_safe("<div class='card'><img src='%s' class='card-img-top' alt='garment'><div class='card-body'><p class='card-text'>%s</p></div></div>"
                            % (obj.image.url, obj.name))

class OutfitForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(OutfitForm, self).__init__(*args, **kwargs)
        self.fields['tops'].queryset = Top.objects.filter(user=self.request.user)
        self.fields['bottoms'].queryset = Bottom.objects.filter(user=self.request.user)
        self.fields['outerwear'].queryset = Outerwear.objects.filter(user=self.request.user)
        self.fields['footwear'].queryset = Footwear.objects.filter(user=self.request.user)
        self.fields['accessories'].queryset = Accessory.objects.filter(user=self.request.user)
    
    class Meta:
        model = Outfit
        fields = ['name', 'image', 'description', 'tops', 'bottoms', 'outerwear', 'footwear', 'accessories']

    tops = CustomMultipleChoiceField(
        queryset=None,
        widget=forms.CheckboxSelectMultiple,
        required=False)

    bottoms = CustomMultipleChoiceField(
        queryset=None,
        widget=forms.CheckboxSelectMultiple,
        required=True)

    outerwear = CustomMultipleChoiceField(
        queryset=None,
        widget=forms.CheckboxSelectMultiple,
        required=False)
    
    footwear = CustomMultipleChoiceField(
        queryset=None,
        widget=forms.CheckboxSelectMultiple,
        required=True)

    accessories = CustomMultipleChoiceField(
        queryset=None,
        widget=forms.CheckboxSelectMultiple,
        required=False)