from django.urls import path
import vendor.views

urlpatterns = [
    path('apply/', vendor.views.create_vendor, name='create_vendor_route'),
    path('profile/', vendor.views.view_vendor_profile, name='view_vendor_profile_route'),
    path('profile/<vendor_profile_id>', vendor.views.edit_vendor_profile, name='edit_vendor_profile_route'),
    path('profile/delete/<vendor_profile_id>', vendor.views.delete_vendor_profile, name='delete_vendor_profile_route')

]