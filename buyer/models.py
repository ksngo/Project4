from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from location.models import Town, Postal
from food.models import Food

# Create your models here.


class Buyer(models.Model):
    town = models.ForeignKey(Town, null=True, blank=False, on_delete=models.SET_NULL)
    postal_code = models.ForeignKey(Postal, null=True, blank=False, on_delete=models.SET_NULL) 
    block = models.PositiveSmallIntegerField( null=False, blank=False)
    street = models.CharField(max_length=254, null=False, blank=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    contact = models.PositiveIntegerField(validators=[MinValueValidator(10000000), MaxValueValidator(99999999)], null=False, blank=False)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.username


class Bookmark(models.Model):
    food = models.ForeignKey(Food, null=False, blank=False, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Buyer, null=False, blank=False, on_delete=models.CASCADE)



