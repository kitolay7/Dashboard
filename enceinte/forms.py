from django import forms
from .models import *

class LocationChoiceField(forms.Form):

    locations = forms.ModelChoiceField(
        queryset=Hostname.objects.values_list("ip_adress", flat=True).distinct(),
        empty_label=None
    )