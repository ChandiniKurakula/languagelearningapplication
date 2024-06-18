from django import forms
from .models import Duolingo

class DuolingoForm(forms.ModelForm):
    class Meta:
         model = Duolingo
         fields = ['title','description']
         widgets = {
             'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title Number'}),
             'description': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter  description'}),
}