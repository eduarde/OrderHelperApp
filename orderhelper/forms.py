from django import forms

from .models import Persoana, Proiect, Furnizor, Producator, Reper

class PersoanaForm(forms.ModelForm):

    class Meta:
        model = Persoana
        fields = ('nume', 'prenume', 'telefon',)
 
class ProiectForm(forms.ModelForm):

	class Meta:
		model = Proiect
		fields = ('titlu','descriere','group',)
		widgets = {
			'titlu': forms.TextInput(attrs={'class': 'form-control'}),
			'descriere': forms.TextInput(attrs={'class': 'form-control'}),
            'group': forms.CheckboxSelectMultiple(),
        }

class FurnizorForm(forms.ModelForm):

	class Meta:
		model = Furnizor
		fields = ('nume','descriere','telefon','group',)
		widgets = {
			'nume': forms.TextInput(attrs={'class': 'form-control'}),
			'descriere': forms.TextInput(attrs={'class': 'form-control'}),
			'telefon': forms.TextInput(attrs={'class': 'form-control'}),
            'group': forms.CheckboxSelectMultiple(),
        }

class ProducatorForm(forms.ModelForm):

	class Meta:
		model = Producator
		fields = ('nume','descriere','telefon','group',)
		widgets = {
			'nume': forms.TextInput(attrs={'class': 'form-control'}),
			'descriere': forms.TextInput(attrs={'class': 'form-control'}),
			'telefon': forms.TextInput(attrs={'class': 'form-control'}),
            'group': forms.CheckboxSelectMultiple(),
        }

class ReperForm(forms.ModelForm):

	class Meta:
		model = Reper
		fields = ('cod_reper','reper','link','group',)
		widgets = {
			'cod_reper': forms.TextInput(attrs={'class': 'form-control'}),
			'reper': forms.TextInput(attrs={'class': 'form-control'}),
			'link': forms.TextInput(attrs={'class': 'form-control'}),
            'group': forms.CheckboxSelectMultiple(),
        }