from django import forms
from .models import Logsheet

class NewBookout(forms.ModelForm):
    pilot = forms.CharField(widget=forms.TextInput(),max_length=30)
    logDate = forms.DateField(widget=forms.DateInput())
    logTime = forms.CharField(widget=forms.TimeInput())
    logFrom = 'EGHP'
    logTo = forms.CharField(widget=forms.TextInput(),max_length=30)
    logAircraftType = forms.CharField(widget=forms.TextInput(),max_length=30)
    logAircraftReg = forms.CharField(widget=forms.TextInput(),max_length=10)
    logPax = forms.IntegerField(widget=forms.NumberInput())
    logDorA = 'D'

    class Meta:
        model = Logsheet
        fields = ['pilot', 'logDate', 'logTime', 'logTo', 'logAircraftType', 'logAircraftReg', 'logPax']


class NewBookin(forms.ModelForm):
    pilot = forms.CharField(widget=forms.TextInput(),max_length=30)
    logDate = forms.DateField(widget=forms.DateInput())
    logTime = forms.CharField(widget=forms.TimeInput())
    logTo = 'EGHP'
    logFrom = forms.CharField(widget=forms.TextInput(),max_length=30)
    logAircraftType = forms.CharField(widget=forms.TextInput(),max_length=30)
    logAircraftReg = forms.CharField(widget=forms.TextInput(),max_length=10)
    logPax = forms.IntegerField(widget=forms.NumberInput())
    logDorA = 'A'

    class Meta:
        model = Logsheet
        fields = ['pilot', 'logDate', 'logTime', 'logFrom', 'logAircraftType', 'logAircraftReg', 'logPax']

