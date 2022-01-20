from django import forms
from .models import Parties


class PartyForm(forms.ModelForm):
    class Meta:
        model = Parties
        fields = '__all__'
        exclude = ('user', 'code')

