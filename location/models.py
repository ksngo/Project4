from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Town(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Postal(models.Model):
    postal_code = models.PositiveIntegerField(validators=[MinValueValidator(10000), MaxValueValidator(999999)], null=False, blank=False)

    def __str__(self):
        return self.postal_code