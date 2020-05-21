from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import Food
from .forms import FoodForm
from vendor.models import Vendor

# Create your views here.


def index(request):


    return render(request, "food/index.html")


@login_required
def view_vendor_food_gallery(request, vendor_profile_id):

    vendor_food_gallery = Food.objects.filter(vendor__id=vendor_profile_id)

    return render(request, "food/vendor_food_gallery.html", {
        "foods": vendor_food_gallery,
        "vendor_profile_id": vendor_profile_id

    })


@login_required
def add_vendor_food(request, vendor_profile_id):

    form = FoodForm()

    if request.method == "POST":

        food_form = FoodForm(request.POST)

        if food_form.is_valid():

            form = food_form.save(commit=False)
            vendor_profile = get_object_or_404(Vendor, pk=vendor_profile_id)
            form.vendor = vendor_profile
            form.save()
            food_form.save_m2m()

            return redirect(reverse(view_vendor_food_gallery, kwargs={"vendor_profile_id": vendor_profile_id}))
        else:

            return render(request, "food/add_vendor_food.html", {
                "form": form,
                "vendor_profile_id": vendor_profile_id
            })

    else:

        return render(request, "food/add_vendor_food.html", {
            "form": form,
            "vendor_profile_id": vendor_profile_id
        })


@login_required
def edit_vendor_food(request, vendor_profile_id, vendor_food_id):

    vendor_food = get_object_or_404(Food, pk=vendor_food_id)

    if request.method == "POST":
        food_form = FoodForm(request.POST, instance=vendor_food)
        if food_form.is_valid():
            form = food_form.save(commit=False)
            vendor_profile = get_object_or_404(Vendor, pk=vendor_profile_id)
            form.vendor = vendor_profile
            form.date_edited = datetime.now()
            form.save()
            food_form.save_m2m()

            return redirect(reverse(view_vendor_food_gallery, kwargs={"vendor_profile_id": vendor_profile_id}))

        else:

            return redirect(reverse(edit_vendor_food, kwargs={"vendor_profile_id":vendor_profile_id, "vendor_food_id": vendor_food_id}))

    else:
        food_form = FoodForm(instance=vendor_food)

        return render(request, "food/edit_vendor_food.html", {
            "form": food_form,
            "vendor_profile_id": vendor_profile_id
        })


@login_required
def delete_vendor_food(request, vendor_profile_id, vendor_food_id):

    vendor_food = get_object_or_404(Food, pk=vendor_food_id)

    if request.method == "POST":
        vendor_food.delete()
        return redirect(reverse(view_vendor_food_gallery, kwargs={"vendor_profile_id": vendor_profile_id}))

    else:

        return render(request, "food/delete_vendor_food.html", {
            "food": vendor_food,
            "vendor_profile_id": vendor_profile_id
        })


