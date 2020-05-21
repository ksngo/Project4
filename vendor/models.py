from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.title


class VendorDeliveryPostal(models.Model):

    postal_code = models.PositiveIntegerField( null=False, blank=False)

    def __str__(self):
        return str(self.postal_code)


class VendorDeliveryTown(models.Model):

    town = models.CharField( max_length=100, null=False, blank=False) 

    def __str__(self):
        return str(self.town)


class Vendor(models.Model):
    category = models.ManyToManyField(Category)
    postal_code = models.PositiveIntegerField( null=False, blank=False)
    name = models.CharField( max_length=100, null=False, blank=False) 
    block = models.PositiveSmallIntegerField( null=False, blank=False)
    street = models.CharField(max_length=254, null=False, blank=False)
    contact = models.PositiveIntegerField(validators=[MinValueValidator(10000000), MaxValueValidator(99999999)], null=False, blank=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    user_contact = models.PositiveIntegerField(validators=[MinValueValidator(10000000), MaxValueValidator(99999999)], null=False, blank=False)
    license_number = models.CharField(max_length=10, null=False, blank=False)
    license_check = models.BooleanField(default=False)
    photo_url=models.URLField(max_length=1024, null=True, blank=True)
    vendordeliverytown = models.ManyToManyField(VendorDeliveryTown)
    vendordeliverypostal = models.ManyToManyField(VendorDeliveryPostal)

    def __str__(self):
        return self.name



