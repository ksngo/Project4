from django.urls import path
import buyer.views

urlpatterns = [
    path('create_profile/', buyer.views.create_buyer_profile, name='create_buyer_profile_route'),
]