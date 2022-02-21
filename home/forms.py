from django import forms
from .models import Pumps


class UtilityForm(forms.ModelForm):
    class Meta:
        model = Pumps
        fields = '__all__'







