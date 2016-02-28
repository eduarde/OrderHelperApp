from django import forms

from .models import Persoana, Proiect, Furnizor, Producator, Reper, Comanda

class PersoanaForm(forms.ModelForm):

    class Meta:
        model = Persoana
        fields = ('nume', 'prenume', 'telefon','group',)
        widgets = {
			'nume': forms.TextInput(attrs={'class': 'form-control'}),
			'prenume': forms.TextInput(attrs={'class': 'form-control'}),
			'telefon': forms.TextInput(attrs={'class': 'form-control'}),
            'group': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
 
class ProiectForm(forms.ModelForm):

	class Meta:
		model = Proiect
		fields = ('titlu','descriere','group',)
		widgets = {
			'titlu': forms.TextInput(attrs={'class': 'form-control'}),
			'descriere': forms.TextInput(attrs={'class': 'form-control'}),
            'group': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

class FurnizorForm(forms.ModelForm):

	class Meta:
		model = Furnizor
		fields = ('nume','descriere','telefon','group',)
		widgets = {
			'nume': forms.TextInput(attrs={'class': 'form-control'}),
			'descriere': forms.TextInput(attrs={'class': 'form-control'}),
			'telefon': forms.TextInput(attrs={'class': 'form-control'}),
            'group': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

class ProducatorForm(forms.ModelForm):

	class Meta:
		model = Producator
		fields = ('nume','descriere','telefon','group',)
		widgets = {
			'nume': forms.TextInput(attrs={'class': 'form-control'}),
			'descriere': forms.TextInput(attrs={'class': 'form-control'}),
			'telefon': forms.TextInput(attrs={'class': 'form-control'}),
            'group': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

class ReperForm(forms.ModelForm):

	class Meta:
		model = Reper
		fields = ('cod_reper','reper','link','group',)
		widgets = {
			'cod_reper': forms.TextInput(attrs={'class': 'form-control'}),
			'reper': forms.TextInput(attrs={'class': 'form-control'}),
			'link': forms.TextInput(attrs={'class': 'form-control'}),
            'group': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

class ComandaForm(forms.ModelForm):

	class Meta:
		model = Comanda
		fields = ('numar_unic','obiect_succint','solicitant','proiect','group',)
		widgets = {
			'numar_unic': forms.TextInput(attrs={'class': 'form-control'}),
			'obiect_succint': forms.TextInput(attrs={'class': 'form-control'}),
			'solicitant': forms.Select(attrs={'class': 'form-control'}),
			'proiect': forms.Select(attrs={'class': 'form-control'}),
            'group': forms.SelectMultiple(attrs={'class': 'form-control'}),
		}