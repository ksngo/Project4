from django.shortcuts import render, reverse, get_object_or_404, HttpResponse
from django.conf import settings
from django.contrib.sites.models import Site
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required
# def checkout(request):

#     stripe.api_key = settings.STRIPE_SECRET_KEY

#     cart = request.session.get('shopping_cart', {})

#     line_items = []
