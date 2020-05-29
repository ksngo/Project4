import uuid

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from food.models import Food
from buyer.models import Buyer

# Create your models here.


class Review(models.Model):
    description = models.TextField(null=True, blank=True)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], null=False, blank=False)
    date_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)


class Comment(models.Model):
    description = models.TextField(null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    review = models.ForeignKey(Review, null=False, blank=False, on_delete=models.CASCADE)


class Process(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.title


class Order(models.Model):
    order_number = models.CharField(max_length=200, null=False, editable=False)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    datetime = models.DateTimeField(auto_now_add=True)
    alternative_delivery_address = models.TextField(null=True, blank=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    # def _generate_order_number(self):
    #     return uuid.uuid4().hex.upper() 

    # def save(self, *args, **kwargs):

    #     if not self.order_number:
    #         self.order_number = self._generate_order_number()
    #     super().save(*args, **kwargs)

    # end of reference

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE )
    review = models.ForeignKey(Review, null=True, blank=True, on_delete=models.SET_NULL)
    process = models.ForeignKey(Process, null=True, blank=False, on_delete=models.SET_NULL)
    food = models.ForeignKey(Food, null=False, blank=False, on_delete=models.DO_NOTHING)
    datetime = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(99)], null=False, blank=False)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    buyer = models.ForeignKey(Buyer, null=True, blank=False, on_delete=models.SET_NULL)



