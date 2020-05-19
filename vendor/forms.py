from django import forms
from .models import Vendor, Vendor_Deliver_To_Town, Vendor_Deliver_To_Postal


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ('name', 'block', 'street', 'postal_code', 'contact', 'user_contact', 'category', 'license_number', 'license_check', 'photo_url')


class DeliverTownForm(forms.ModelForm):
    class Meta:
        model = Vendor_Deliver_To_Town
        fields = ('town',)


class DeliverPostalForm(forms.ModelForm):
    class Meta:
        model = Vendor_Deliver_To_Postal
        fields = ('postal_code',)
