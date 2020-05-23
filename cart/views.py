from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from food.models import Food
from buyer.models import Buyer


# Create your views here.

@login_required
def add_to_cart(request, buyer_id, food_id):

    cart = request.session.get('shopping_cart', {})

    b = get_object_or_404(Buyer, pk=buyer_id)
    buyer = model_to_dict(b)

    food = get_object_or_404(Food, pk=food_id)

    if buyer_id not in cart:
        print("buyer not in cart")
        cart[buyer_id] = {food_id: {
            "food_id": food_id,
            "vendor_name": food.vendor.name,
            "food_title": food.title,
            "price": str(food.price),
            "qty": 1,
            "buyer": buyer
        }}

        messages.success(request, f" {food.title} from {food.vendor.name} added to cart.")

    else:
        if food_id in cart[buyer_id] :
            print("buyer already in cart, and same food")
            cart[buyer_id][food_id]["qty"] += 1

            messages.success(request, f" {food.title} from {food.vendor.name} added to cart.")

        else:
            print("buyer already in cart, but different food")
            cart[buyer_id][food_id] = {
                "food_id": food_id,
                "vendor_name": food.vendor.name,
                "food_title": food.title,
                "price": str(food.price),
                "qty": 1,
                "buyer": buyer
            }

            messages.success(request, f" {food.title} from {food.vendor.name} added to cart.")

    # print(cart)
    request.session['shopping_cart'] = cart

    return redirect(reverse("index_by_profile_route", kwargs={"buyer_id": buyer_id}))


@login_required
def view_cart(request):

    cart = request.session.get("shopping_cart", {})

    return render(request, "cart/view_cart.html", {
        "cart": cart
    })


@login_required
def remove_from_cart(request, buyer_id, food_id):

    cart = request.session.get("shopping_cart")
    food = get_object_or_404(Food, pk=food_id)
    buyer = get_object_or_404(Buyer, pk=buyer_id)

    if buyer_id in cart:
        if food_id in cart[buyer_id]:

            del cart[buyer_id][food_id]

            request.session["shopping_cart"] = cart

            messages.success(request, f" {food.title} from {food.vendor.name} removed. Ordered by '{buyer}'.")

    return redirect(reverse(view_cart))


@login_required
def add_quantity(request, buyer_id, food_id):

    cart = request.session.get("shopping_cart")

    if request.method == "POST":
        if buyer_id in cart:
            if food_id in cart[buyer_id]:

                cart[buyer_id][food_id]["qty"] += 1
                request.session['shopping_cart'] = cart

    return redirect(reverse(view_cart))


@login_required
def subtract_quantity(request, buyer_id, food_id):

    cart = request.session.get("shopping_cart")

    if request.method == "POST":
        if buyer_id in cart:
            if food_id in cart[buyer_id]:

                if cart[buyer_id][food_id]["qty"] > 0:
                    cart[buyer_id][food_id]["qty"] -= 1
                    request.session['shopping_cart'] = cart
                else:

                    cart[buyer_id][food_id]["qty"] = 0
                    request.session['shopping_cart'] = cart

    return redirect(reverse(view_cart))
