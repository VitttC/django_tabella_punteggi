from django import forms
from punti.models import Punti


class ScoreForm(forms.ModelForm):
    class Meta:
        model = Punti
        fields = ['name', 'value']