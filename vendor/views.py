from django.shortcuts import render, get_object_or_404, reverse, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import VendorForm, DeliverTownForm, DeliverPostalForm
from .models import Vendor, Vendor_Deliver_To_Town, Vendor_Deliver_To_Postal


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
            
            return redirect(reverse(view_vendor_profiles))
            
        else:
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

            return redirect(reverse(view_vendor_profiles))
        
        else:

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

        return redirect(reverse(view_vendor_profiles))

    else:
        
        return render(request, "vendor/vendor_delete_profile.html")


def create_delivery_area(request, vendor_profile_id):

    if request.method == "POST":

        town_form = DeliverTownForm(request.POST)
        postal_form = DeliverPostalForm(request.POST)

        vendor_profile = get_object_or_404(Vendor, pk=vendor_profile_id )

        if town_form.is_valid():
            form = town_form.save(commit=False)
            form.vendor = vendor_profile
            form.save()
        
        if postal_form.is_valid():
            form = postal_form.save(commit=False)
            form.vendor = vendor_profile
            form.save()

        return redirect(reverse(create_delivery_area, kwargs={'vendor_profile_id': vendor_profile_id}))
    
    else:
         
        town_form = DeliverTownForm()
        postal_form = DeliverPostalForm()

        towns = Vendor_Deliver_To_Town.objects.filter(vendor__id=vendor_profile_id)
        postals = Vendor_Deliver_To_Postal.objects.filter(vendor__id=vendor_profile_id)

        return render(request, "vendor/vendor_delivery_area.html", {
            "towns": towns,
            "postals": postals,
            "town_form": town_form,
            "postal_form": postal_form,
            "vendor_profile_id": vendor_profile_id
        })


def remove_town_vendor(request, vendor_profile_id, town_vendor_id):

    town_vendor = get_object_or_404(Vendor_Deliver_To_Town, pk=town_vendor_id)
    town_vendor.delete()

    return redirect(reverse(create_delivery_area, kwargs={'vendor_profile_id': vendor_profile_id}))


def remove_postal_vendor(request, vendor_profile_id, postal_vendor_id):

    postal_vendor = get_object_or_404(Vendor_Deliver_To_Postal, pk=postal_vendor_id)
    postal_vendor.delete()

    return redirect(reverse(create_delivery_area, kwargs={'vendor_profile_id': vendor_profile_id}))
