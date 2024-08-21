from django import forms

class PredictionForm(forms.Form):
    text_input = forms.CharField(widget=forms.Textarea)