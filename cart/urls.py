from django.urls import path
import cart.views

urlpatterns = [
    path('/<buyer_id>/add/<food_id>', cart.views.add_to_cart, name="add_to_cart_route")
]