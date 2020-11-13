from django import forms

class PreguntaForm(forms.Form):
    asunto = forms.CharField(max_length=100, required=True)
    descrip = forms.CharField(widget=forms.Textarea, required=True)