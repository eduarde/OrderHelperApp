from django import forms

from .models import Persoana

class PersoanaForm(forms.ModelForm):

    class Meta:
        model = Persoana
        fields = ('nume', 'prenume', 'telefon',)