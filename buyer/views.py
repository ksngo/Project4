from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib.auth.decorators import login_required
from .models import Buyer
from .forms import BuyerForm

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
            return HttpResponse("profile is saved")
        else:
            return redirect(reverse(create_buyer_profile))

    else:

        return render(request, "buyer/create_buyer_profile.html", {
            "form": buyer_form
        })

    

