from django.contrib import admin
from .models import Category, Vendor, Vendor_Deliver_To_Town, Vendor_Deliver_To_Postal
# Register your models here.

admin.site.register(Category)
admin.site.register(Vendor)
admin.site.register(Vendor_Deliver_To_Town)
admin.site.register(Vendor_Deliver_To_Postal)
