from django.contrib import admin
from .models import Order, Order_line_item, Process, Review, Comment

# Register your models here.
admin.site.register(Order)
admin.site.register(Order_line_item)
admin.site.register(Process)
admin.site.register(Review)
admin.site.register(Comment)


