from django import forms
from .models import Vendor, VendorDeliveryTown, VendorDeliveryPostal


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ('name', 'block', 'street', 'postal_code', 'contact', 'user_contact', 'category', 'license_number', 'photo_url')

    def __init__(self, *args, **kwargs): 
        super(VendorForm, self).__init__(*args, **kwargs)
        self.fields['license_number'].disabled = True
        self.fields['name'].disabled = True
        self.fields['block'].disabled = True
        self.fields['street'].disabled = True
        self.fields['postal_code'].disabled = True


class DeliverTownForm(forms.ModelForm):
    class Meta:
        model = VendorDeliveryTown
        fields = ('town',)


class DeliverPostalForm(forms.ModelForm):
    class Meta:
        model = VendorDeliveryPostal
        fields = ('postal_code',)
