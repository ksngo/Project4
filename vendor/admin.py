from django.contrib import admin
from .models import Category, Vendor, VendorDeliveryTown, VendorDeliveryPostal
# Register your models here.

admin.site.register(Category)
admin.site.register(Vendor)
admin.site.register(VendorDeliveryTown)
admin.site.register(VendorDeliveryPostal)
