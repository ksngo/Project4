from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from vendor.models import Vendor


# Create your models here.


class Tag(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.title

class Food(models.Model):
    vendor = models.ForeignKey(Vendor, null=False, blank=False, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    portion = models.PositiveSmallIntegerField( validators=[MinValueValidator(1), MaxValueValidator(99)] , default=1, null=False, blank=False )
    price = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now_add=True)
    photo_url = models.URLField(max_length=1024, null=True, blank=True)
    delivery_time = models.DecimalField(max_digits=3, decimal_places=0, null=False, blank=False)

    def __str__(self):
        return self.title

