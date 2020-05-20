from django import forms
from .models import Buyer


class BuyerForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = ("block", "street", "postal_code", "town", "contact")



