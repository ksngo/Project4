from django.shortcuts import render, reverse, get_object_or_404, HttpResponse
from django.conf import settings
from django.contrib.sites.models import Site
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import stripe
from food.models import Food

# Create your views here.

endpoint_secret = settings.SIGNING_SECRET


@login_required
def checkout(request):

    stripe.api_key = settings.STRIPE_SECRET_KEY

    cart = request.session.get('shopping_cart', {})

    line_items = []

    for b_key, b_value in cart.items():
        for f_key, f_value in b_value.items():
            food_object = get_object_or_404(Food, pk=f_value["food_id"])
            line_items.append({
                'name': f"{food_object.title},{f_value['food_id']}",
                'amount': int(food_object.price*100),
                'currency': 'sgd',
                'quantity': f_value["qty"],
                'description': f"{f_value['buyer']['id']},{f_value['buyer']['town']},{f_value['buyer']['postal_code']}"
            })

    current_site = Site.objects.get_current()
    domain = current_site.domain

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        success_url=domain + reverse(checkout_success),
        cancel_url=domain + reverse(checkout_cancelled)
    )

    return render(request, "checkout/checkout.html", {
        "session_id": session.id,
        "public_key": settings.STRIPE_PUBLISHABLE_KEY
    })

@login_required
def checkout_success(request):
    request.session['shopping_cart'] = {}
    return HttpResponse("checkout success")

@login_required
def checkout_cancelled(request):
    return HttpResponse("checkout cancelled")


@csrf_exempt
def payment_completed(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )

    except ValueError as e:
        print(e)
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        print(e)
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        # Fulfill the purchase...
        handle_checkout_session(session)

    return HttpResponse(status=200)


def handle_checkout_session(session):

    print(session)
