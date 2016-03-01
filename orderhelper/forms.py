from django import forms
from datetimewidget.widgets import DateWidget
from .models import Persoana, Proiect, Furnizor, Producator, Reper, Comanda, Subcomanda


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
			'numar_unic': forms.NumberInput(attrs={'class': 'form-control'}),
			'obiect_succint': forms.TextInput(attrs={'class': 'form-control'}),
			'solicitant': forms.Select(attrs={'class': 'form-control'}),
			'proiect': forms.Select(attrs={'class': 'form-control'}),
            'group': forms.SelectMultiple(attrs={'class': 'form-control'}),
		}

class SubcomandaForm(forms.ModelForm):

	class Meta:
		model = Subcomanda
		fields = ('comanda_ref','producator','reper','furnizor','cantitate','pret','termen_plata','mod_plata','data_livrare','group',)
		dateOptions = {
			'format': 'mm/dd/yyyy',
			'autoclose': True
		}
		widgets = {
			'comanda_ref': forms.Select(attrs={'class': 'form-control'}),
			'producator': forms.Select(attrs={'class': 'form-control'}),
			'reper': forms.Select(attrs={'class': 'form-control'}),
			'furnizor': forms.Select(attrs={'class': 'form-control'}),
			'cantitate': forms.NumberInput(attrs={'class': 'form-control'}),
			'pret': forms.NumberInput(attrs={'class': 'form-control'}),
			'termen_plata': forms.Select(attrs={'class': 'form-control'}),
			'mod_plata': forms.Select(attrs={'class': 'form-control'}),
			'data_livrare': DateWidget(attrs={'id':"idlivrare"}, bootstrap_version=3, options = dateOptions),
            'group': forms.SelectMultiple(attrs={'class': 'form-control'}),
		}