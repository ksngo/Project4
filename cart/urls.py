from django.urls import path
import cart.views

urlpatterns = [
    path('<buyer_id>/add/<food_id>', cart.views.add_to_cart, name="add_to_cart_route"),
    path('', cart.views.view_cart, name="view_cart_route"),
    path('remove/<food_id>/for/<buyer_id>', cart.views.remove_from_cart, name="remove_from_cart_route"),
    path('add_qty/<food_id>/for/<buyer_id>', cart.views.add_quantity, name="add_quantity_route"),
    path('subtract_qty/<food_id>/for/<buyer_id>', cart.views.subtract_quantity, name="subtract_quantity_route")
]