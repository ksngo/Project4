from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Buyer
from .forms import BuyerForm
from vendor.models import Vendor

# Create your views here.


@login_required
def create_buyer_profile(request):
    buyer_form = BuyerForm()

    if request.method == "POST":
        buyer_form = BuyerForm(request.POST)

        if buyer_form.is_valid():
            form = buyer_form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect(reverse(show_buyer_profiles))
        else:
            return redirect(reverse(create_buyer_profile))

    else:

        return render(request, "buyer/create_buyer_profile.html", {
            "form": buyer_form
        })


@login_required
def edit_buyer_profile(request, buyer_id):

    buyer_profile = get_object_or_404(Buyer, pk=buyer_id)

    if request.method == "POST":
        buyer_form = BuyerForm(request.POST, instance=buyer_profile)
        buyer_form.save()  # does not require to commit False form to save user as request.user; user still intact in database after the save

        return redirect(reverse(show_buyer_profiles))

    else:

        buyer_form = BuyerForm(instance=buyer_profile)

        return render(request, "buyer/edit_buyer_profile.html", {
            "form": buyer_form
        })


@login_required
def show_buyer_profiles(request):

    buyer_profiles = Buyer.objects.all().filter(user=request.user)

    return render(request, "buyer/buyer_profiles.html", {
        "objects": buyer_profiles
    })

@login_required
def delete_buyer_profile(request, buyer_id):

    buyer_profile = get_object_or_404(Buyer, pk=buyer_id)

    if request.method == "POST":
        buyer_profile.delete()
        return redirect(reverse(show_buyer_profiles))
    
    else:

        return render(request, "buyer/delete_buyer_profile.html", {
            "object" : buyer_profile
        })

@login_required
def index(request):

    buyer_find = Buyer.objects.get(id=3).town
    print(buyer_find)


    v = Vendor.objects.all()[1]
    print(v)
    vendor_find = v.vendordeliverytown_set.all()
    print(vendor_find)

    return HttpResponse("success")