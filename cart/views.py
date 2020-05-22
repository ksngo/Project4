from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from food.models import Food
from buyer.models import Buyer


# Create your views here.

@login_required
def add_to_cart(request, buyer_id, food_id):

    cart = request.session.get('shopping_cart', {})

    b = get_object_or_404(Buyer, pk=buyer_id)
    buyer = model_to_dict(b)
    
    print(buyer)
    food = get_object_or_404(Food, pk=food_id)

    if buyer_id not in cart:
        print("buyer not in cart")
        cart[buyer_id] = {food_id: {
            "food_id": food_id,
            "food_title": food.title,
            "price": str(food.price),
            "qty": 1,
            "buyer": buyer
        }}

    else:
        if food_id in cart[buyer_id] :
            print("buyer already in cart, and same food")
            cart[buyer_id][food_id]["qty"] += 1

        else:
            print("buyer already in cart, but different food")
            cart[buyer_id][food_id] = {
                "food_id": food_id,
                "food_title": food.title,
                "price": str(food.price),
                "qty": 1,
                "buyer": buyer
            }

    print(cart)
    request.session['shopping_cart'] = cart

    return redirect(reverse("index_by_profile_route", kwargs={"buyer_id":buyer_id}))


@login_required
def view_cart(request):

    cart = request.session.get("shopping_cart", {})

    return render(request, "cart/view_cart.html", {
        "cart": cart
    })

