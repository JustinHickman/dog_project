from django import forms
from .models import Dog

class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ['dogname', 'dogbreed', 'dogage', 'dogownerid']
        labels = {'dogname':'Dog Name', 'dogbreed':'Dog Breed', 
                    'dogage':'Dog Age', 'dogownerid':'Owner ID'}
