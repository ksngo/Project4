from django.contrib import admin
from .models import Order, OrderLineItem, Process, Review, Comment

# Register your models here.
admin.site.register(Order)
admin.site.register(OrderLineItem)
admin.site.register(Process)
admin.site.register(Review)
admin.site.register(Comment)


