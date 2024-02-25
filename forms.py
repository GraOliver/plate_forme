from django import forms
from .models import  Communaute

class FormCommunaute (forms.ModelForm):
    commune = forms.ModelChoiceField(queryset=Communaute.objects.all(), label="Communautés")
