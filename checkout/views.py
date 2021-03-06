from django.shortcuts import render, reverse, get_object_or_404, HttpResponse
from django.conf import settings
from django.contrib.sites.models import Site
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
import stripe
from food.models import Food
from order.models import Order, OrderLineItem, Process
from buyer.models import Buyer

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
                'name': f"{food_object.title},Id{f_value['food_id']}",
                'amount': int(food_object.price*100),
                'currency': 'sgd',
                'quantity': f_value["qty"],
                'description': f"Id{f_value['buyer']['id']},{f_value['buyer']['town']},{f_value['buyer']['postal_code']}"
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
    return HttpResponse("Checkout Success. Please refresh your shopping cart.")

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

        print("before handle checkout session")
        # Fulfill the purchase...
        handle_checkout_session(session)

        print("after handle checkout session")

    return HttpResponse(status=200)


def handle_checkout_session(session):

    print("hi I am in handlecheckoutsession")
    #  to retrieve the user and create an Order model(order_id)
    print(session.display_items)
    for i in session.display_items:
        print("hi I am in first loop")
        buyer_id = i.custom.description.split(",")[0].replace("Id", "")
        buyer = get_object_or_404(Buyer, pk=buyer_id)
        user_object = buyer.user

        order = Order(order_number=session.id, user=user_object)
        order.save()

        print("order created")
        break

    #  retrieve each line items with same order_id and store in an OrderLineItem model
    for i in session.display_items:
        print("hi I am in second loop")
        print(i)
        buyer_id = i.custom.description.split(",")[0].replace("Id", "")
        print(buyer_id)
        buyer = get_object_or_404(Buyer, pk=buyer_id)
        print(buyer)
        order = get_object_or_404(Order, order_number=session.id)
        print(order)
        process = get_object_or_404(Process, title="undelivered")
        print(process)
        food_id = i.custom.name.split(",")[1].replace("Id","")
        print(food_id)
        food = get_object_or_404(Food, pk=food_id)
        print(food)
        quantity = i.quantity
        cost = (i.amount)*quantity/100
        print(cost)

        order_line_item = OrderLineItem(order=order, process=process, food=food, quantity=quantity, cost=cost, buyer=buyer)
        print(order_line_item)
        order_line_item.save()

        print("end of second loop")




