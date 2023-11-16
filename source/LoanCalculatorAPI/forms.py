from django import forms
from django.forms import ModelForm
from .models import *

class LoanForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter loan title...'}))
    value = forms.IntegerField(widget = forms.NumberInput(attrs={'placeholder':'Enter initial loaned value...'}))
    lending_rate = forms.FloatField(widget = forms.NumberInput(attrs={'placeholder':'Enter the lending rate...'}))
    months = forms.IntegerField(widget = forms.NumberInput(attrs={'placeholder':'Enter duration of the loan in months...'}))
    
    class Meta:
        model = Loan
        fields = ('title','value','lending_rate','months')
