from django import forms
from .models import Vendor

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ('name', 'block', 'street', 'postal_code', 'contact', 'user_contact', 'category', 'license_number', 'license_check', 'photo_url')
        