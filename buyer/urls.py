from django.urls import path
import buyer.views

urlpatterns = [
    path('create_profile/', buyer.views.create_buyer_profile, name='create_buyer_profile_route'),
    path('edit_profile/<buyer_id>', buyer.views.edit_buyer_profile, name="edit_buyer_profile_route"),
    path('my_profiles', buyer.views.show_buyer_profiles, name="show_buyer_profiles_route")
]