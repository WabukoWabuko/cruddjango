from django import forms
from .models import PeopleM

class PeopleForm(forms.ModelForm):
    class Meta:
        model = PeopleM
        fields = ['first_name', 'last_name', 'email', 'phone', 'description', 'image']

 