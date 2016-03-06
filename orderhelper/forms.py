from django import forms
from django.forms import HiddenInput
from datetimewidget.widgets import DateWidget
from .models import Persoana, Proiect, Furnizor, Producator, Reper, Comanda, Subcomanda, Valuta
from datetime import date, datetime, timedelta
from django.utils.timezone import now

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

class ComandaEditForm(forms.ModelForm):

	class Meta:
		model = Comanda
		fields = ('numar_unic','status','obiect_succint','solicitant','proiect','group',)
		widgets = {
			'numar_unic': forms.NumberInput(attrs={'class': 'form-control'}),
			'status': forms.Select(attrs={'class': 'form-control'}),
			'obiect_succint': forms.TextInput(attrs={'class': 'form-control'}),
			'solicitant': forms.Select(attrs={'class': 'form-control'}),
			'proiect': forms.Select(attrs={'class': 'form-control'}),
            'group': forms.SelectMultiple(attrs={'class': 'form-control'}),
		}

class SubcomandaForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(SubcomandaForm, self).__init__(*args, **kwargs)
		self.fields['comanda_ref'].queryset = Comanda.objects.filter(status__text='Deschis')

	class Meta:
		model = Subcomanda
		fields = ('comanda_ref','producator','reper','furnizor','cantitate','pret','valuta','termen_plata','mod_plata','data_livrare','group',)
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
			'valuta': forms.Select(attrs={'class': 'form-control'}),
			'termen_plata': forms.Select(attrs={'class': 'form-control'}),
			'mod_plata': forms.Select(attrs={'class': 'form-control'}),
			'data_livrare': DateWidget(attrs={'id':"idlivrare"}, bootstrap_version=3, options = dateOptions),
            'group': forms.SelectMultiple(attrs={'class': 'form-control'}),
		}

class SubcomandaEditForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(SubcomandaEditForm, self).__init__(*args, **kwargs)
		self.fields['comanda_ref'].queryset = Comanda.objects.filter(status__text='Deschis')

	class Meta:
		model = Subcomanda
		fields = ('comanda_ref','status','producator','reper','furnizor','cantitate','pret','valuta','termen_plata','mod_plata','data_livrare','group',)
		dateOptions = {
			'format': 'mm/dd/yyyy',
			'autoclose': True
		}
		widgets = {
			'comanda_ref': forms.Select(attrs={'class': 'form-control'}),
			'status': forms.Select(attrs={'class': 'form-control'}),
			'producator': forms.Select(attrs={'class': 'form-control'}),
			'reper': forms.Select(attrs={'class': 'form-control'}),
			'furnizor': forms.Select(attrs={'class': 'form-control'}),
			'cantitate': forms.NumberInput(attrs={'class': 'form-control'}),
			'pret': forms.NumberInput(attrs={'class': 'form-control'}),
			'valuta': forms.Select(attrs={'class': 'form-control'}),
			'termen_plata': forms.Select(attrs={'class': 'form-control'}),
			'mod_plata': forms.Select(attrs={'class': 'form-control'}),
			'data_livrare': DateWidget(attrs={'id':"idlivrare"}, bootstrap_version=3, options = dateOptions),
            'group': forms.SelectMultiple(attrs={'class': 'form-control'}),
		}

class SubcomandaCloseForm(forms.ModelForm):
	
	def __init__(self, *args, **kwargs):
		super(SubcomandaCloseForm, self).__init__(*args, **kwargs)
		self.fields['data_primire'].initial = datetime.now()

	class Meta:
		model = Subcomanda
		fields = ('data_primire',)
		dateOptions = {
			'format': 'mm/dd/yyyy',
			'autoclose': True
		}
		widgets = {
			'data_primire': DateWidget(attrs={'id':"idprimire"}, bootstrap_version=3, options = dateOptions),
		}

class ComandaCloseForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(ComandaCloseForm, self).__init__(*args, **kwargs)
		self.fields['data_primire'].initial = datetime.now()

	class Meta:
		model = Comanda
		fields = ('data_primire',)
		dateOptions = {
			'format': 'mm/dd/yyyy',
			'autoclose': True
		}
		widgets = {
			'data_primire': DateWidget(attrs={'id':"idprimire"}, bootstrap_version=3, options = dateOptions),
		}


class SubcomandaCancelForm(forms.ModelForm):

	class Meta:
		model = Subcomanda
		fields = ('data_primire','numar_curent',)
		dateOptions = {
			'format': 'mm/dd/yyyy',
			'autoclose': True
		}
		widgets = {
			'data_primire': DateWidget(attrs={'id':"idprimire"}, bootstrap_version=3, options = dateOptions),
			'numar_curent': HiddenInput(),
		}
		
class ComandaCancelForm(forms.ModelForm):

	class Meta:
		model = Comanda
		fields = ('data_primire','numar_unic',)
		dateOptions = {
			'format': 'mm/dd/yyyy',
			'autoclose': True
		}
		widgets = {
			'data_primire': DateWidget(attrs={'id':"idprimire"}, bootstrap_version=3, options = dateOptions),
			'numar_unic': HiddenInput(),
		}
