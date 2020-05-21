from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from food.models import Food

# Create your models here.


class Buyer(models.Model):
    town = models.CharField(max_length=100, null=True, blank=False)
    postal_code = models.PositiveIntegerField(null=False, blank=False) 
    block = models.PositiveSmallIntegerField( null=False, blank=False)
    street = models.CharField(max_length=254, null=False, blank=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    contact = models.PositiveIntegerField(validators=[MinValueValidator(10000000), MaxValueValidator(99999999)], null=False, blank=False)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return '%s, %s %s (%s), %s' % (self.user.username, self.block, self.street, self.postal_code, self.town)


class Bookmark(models.Model):
    food = models.ForeignKey(Food, null=False, blank=False, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Buyer, null=False, blank=False, on_delete=models.CASCADE)



