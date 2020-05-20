from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
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

