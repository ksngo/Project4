from django.urls import path
import buyer.views

urlpatterns = [
    path('create_profile/', buyer.views.create_buyer_profile, name='create_buyer_profile_route'),
    path('edit_profile/<buyer_id>', buyer.views.edit_buyer_profile, name="edit_buyer_profile_route"),
    path('my_profiles', buyer.views.show_buyer_profiles, name="show_buyer_profiles_route"),
    path('delete_profile/<buyer_id>', buyer.views.delete_buyer_profile, name="delete_buyer_profile_route"),
    path('index/', buyer.views.index, name='index_route'),
    path('index/<buyer_id>', buyer.views.index_by_profile, name='index_by_profile_route'),
    path('my_orders', buyer.views.view_order_history, name='view_order_history_route'),
    path('', buyer.views.view_home, name="view_home_route")
]