from django.shortcuts import render, get_object_or_404, reverse, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import VendorForm
from .models import Vendor

# Create your views here.

@login_required
def view_vendor_profile(request):
    vendor_profile = Vendor.objects.filter(user=request.user)
    
    # get_object_or_404(Vendor, pk=vendor_id)

    return render(request, "vendor/vendor_profile.html", {
            "vendor_profile": vendor_profile
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
            
            return redirect(reverse(view_vendor_profile))
            
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

            return redirect(reverse(view_vendor_profile))
        
        else:

            return redirect(reverse(edit_vendor_profile, kwargs={'vendor_profile_id': vendor_profile_id}))

    else:

        return render(request, "vendor/vendor_profile_detail.html", {
            "form": profile_form
        })


