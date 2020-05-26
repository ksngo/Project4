from django import forms
from .models import Vendor, VendorDeliveryTown, VendorDeliveryPostal


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ('name', 'block', 'street', 'postal_code', 'contact', 'user_contact', 'category', 'license_number', 'photo_url')

class DeliverTownForm(forms.ModelForm):
    class Meta:
        model = VendorDeliveryTown
        fields = ('town',)


class DeliverPostalForm(forms.ModelForm):
    class Meta:
        model = VendorDeliveryPostal
        fields = ('postal_code',)
