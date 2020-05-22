from django.urls import path
import cart.views

urlpatterns = [
    path('/<buyer_id>/add/<food_id>', cart.views.add_to_cart, name="add_to_cart_route"),
    path('', cart.views.view_cart, name="view_cart_route"),
    path('remove/<food_id>/for/<buyer_id>', cart.views.remove_from_cart, name="remove_from_cart_route")
]