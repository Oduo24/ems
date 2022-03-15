from django import forms
from .models import Pumps, FlowMeter


class UtilityForm(forms.ModelForm):
    class Meta:
        model = Pumps
        fields = '__all__'


class FlowMeterForm(forms.ModelForm):
    class Meta:
        model = FlowMeter
        fields = ['date', 'reading1', 'reading2']








