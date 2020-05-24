from django.shortcuts import render, get_object_or_404, reverse, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import VendorForm, DeliverTownForm, DeliverPostalForm
from .models import Vendor, VendorDeliveryTown, VendorDeliveryPostal
from order.models import OrderLineItem


# Create your views here.

@login_required
def view_vendor_profiles(request):
    vendor_profiles = Vendor.objects.filter(user=request.user)
    username = request.user.username

    return render(request, "vendor/vendor_profiles.html", {
            "vendor_profiles": vendor_profiles,
            "username": username
    })


@login_required
def create_vendor(request):

    vendor_form = VendorForm()

    if request.method == 'POST':
        create_form = VendorForm(request.POST)

        if create_form.is_valid():

            form = create_form.save(commit=False)
            form.user = request.user
            form.save()
            messages.success(request, "New vendor added." )

            return redirect(reverse(view_vendor_profiles))

        else:
            messages.warning(request, "Contact number must be 8 digits numbers.")
            return render(request, "vendor/vendor_form.html", {
                'form':  vendor_form
            })

    else:

        return render(request, "vendor/vendor_form.html", {
            'form':  vendor_form
        })


@login_required
def edit_vendor_profile(request, vendor_profile_id):

    profile = get_object_or_404(Vendor, pk=vendor_profile_id)
    profile_form = VendorForm(instance=profile)

    if request.method == "POST":
        create_form = VendorForm(request.POST, instance=profile)

        if create_form.is_valid():

            create_form.save()
            messages.success(request, f" '{profile}'' successfully updated.")
            return redirect(reverse(view_vendor_profiles))

        else:
            messages.warning(request, "Contact number must be 8 digits numbers.")
            return redirect(reverse(edit_vendor_profile, kwargs={'vendor_profile_id': vendor_profile_id}))

    else:

        return render(request, "vendor/vendor_profile_detail.html", {
            "form": profile_form,
            "vendor_profile_id": vendor_profile_id
        })


def delete_vendor_profile(request, vendor_profile_id):

    if request.method == "POST":

        vendor_profile = get_object_or_404(Vendor, pk=vendor_profile_id)
        vendor_profile.delete()
        messages.success(request, f" {vendor_profile} removed.")
        return redirect(reverse(view_vendor_profiles))

    else:

        return render(request, "vendor/vendor_delete_profile.html")


def create_delivery_area(request, vendor_profile_id):

    if request.method == "POST":

        vendor_object = get_object_or_404(Vendor, pk=vendor_profile_id)
        print(vendor_object)
        try:
            ##### adding to manytomany field into vendor_object #####
            town = request.POST["town"]
            f = VendorDeliveryTown.objects.create(town=town)  # create a new town object in VendorDeliveryTown table
            vendor_object.vendordeliverytown.add(f)  # add the town object into Vendor table's town manytomany field

        except:
            postal = request.POST["postal"]
            f = VendorDeliveryPostal.objects.create(postal_code=postal)
            vendor_object.vendordeliverypostal.add(f)

        return redirect(reverse(create_delivery_area, kwargs={'vendor_profile_id': vendor_profile_id}))

    else:

        vendor_object = get_object_or_404(Vendor, pk=vendor_profile_id)
        towns = VendorDeliveryTown.objects.filter(vendor=vendor_object)
        postals = VendorDeliveryPostal.objects.filter(vendor=vendor_object)

        return render(request, "vendor/vendor_delivery_area.html", {
            "towns": towns,
            "postals": postals,
            "vendor_profile_id": vendor_profile_id
        })


def remove_town_vendor(request, vendor_profile_id, town_vendor_id):

    town_vendor = get_object_or_404(VendorDeliveryTown, pk=town_vendor_id)
    town_vendor.delete()

    return redirect(reverse(create_delivery_area, kwargs={'vendor_profile_id': vendor_profile_id}))


def remove_postal_vendor(request, vendor_profile_id, postal_vendor_id):

    postal_vendor = get_object_or_404(VendorDeliveryPostal, pk=postal_vendor_id)
    postal_vendor.delete()

    return redirect(reverse(create_delivery_area, kwargs={'vendor_profile_id': vendor_profile_id}))


def view_vendor_orders(request, vendor_profile_id):
    username = request.user.username
    vendor = Vendor.objects.get(id=vendor_profile_id)

    if request.method == "POST":

        orderlineitem_id = request.POST["special"]

        # o = get_object_or_404(OrderLineItem, pk=orderlineitem_id)
        orderobject = OrderLineItem.objects.get(id=orderlineitem_id)
        order = OrderLineItem(order=orderobject, order__process__title="delivered")
        order.save()

    orders = OrderLineItem.objects.all().filter(food__vendor__id=vendor_profile_id)

    return render(request, "vendor/vendor_orders.html", {
        "orders": orders,
        "vendor": vendor,
        "username": username,
        "vendor_profile_id": vendor_profile_id
    })
