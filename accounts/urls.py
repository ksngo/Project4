from django.urls import path
import accounts.views

urlpatterns = [
    path("view", accounts.views.view_account, name="view_account_route")
]