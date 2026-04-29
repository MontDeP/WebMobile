from django.forms import ModelForm
from django import forms
from veiculo.models import Veiculo


class FormularioVeiculo(ModelForm):

    class Meta:
        model = Veiculo
        exclude = []
        widgets = {
            'marca': forms.Select(attrs={'class': 'form-select'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'ano': forms.NumberInput(attrs={'class': 'form-control'}),
            'cor': forms.Select(attrs={'class': 'form-select'}),
            'combustivel': forms.Select(attrs={'class': 'form-select'}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
