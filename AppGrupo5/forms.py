from django import forms

class CargaInstrumento(forms.Form):
    marca = forms.CharField()
    modelo = forms.CharField()
    tipoinstrumento = forms.CharField()
    color = forms.CharField()
