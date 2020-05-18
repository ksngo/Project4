from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from location.models import Postal, Town

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.title


class Vendor(models.Model):
    category = models.ManyToManyField(Category)
    postal_code = models.ForeignKey(Postal, null=True, blank=False, on_delete=models.SET_NULL)
    name = models.CharField( max_length=100, null=False, blank=False) 
    block = models.PositiveSmallIntegerField( null=False, blank=False)
    street = models.CharField(max_length=254, null=False, blank=False)
    contact = models.PositiveIntegerField(validators=[MinValueValidator(10000000), MaxValueValidator(99999999)], null=False, blank=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    owner_name = models.CharField(max_length=100, null=False, blank=False)
    owner_contact = models.PositiveIntegerField(validators=[MinValueValidator(10000000), MaxValueValidator(99999999)], null=False, blank=False)
    owner_email = models.EmailField(null=True, blank=True)
    license_number = models.CharField(max_length=10, null=False, blank=False)
    license_check = models.BooleanField(default=False)
    photo_url=models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name


class Vendor_Deliver_To_Town(models.Model):
    town = models.ForeignKey(Town, null=False, blank=False, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, null=False, blank=False, on_delete=models.CASCADE)


class Vendor_Deliver_To_Postal(models.Model):
    postal_code = models.ForeignKey(Postal, null=False, blank=False, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, null=False, blank=False, on_delete=models.CASCADE)

