from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
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


@login_required
def edit_buyer_profile(request, buyer_id):

    buyer_profile = get_object_or_404(Buyer, pk=buyer_id)

    if request.method == "POST":
        buyer_form = BuyerForm(request.POST, instance=buyer_profile)
        buyer_form.save()  # does not require to commit False form to save user as request.user; user still intact in database after the save

        return HttpResponse("success update")

    else:

        buyer_form = BuyerForm(instance=buyer_profile)

        return render(request, "buyer/edit_buyer_profile.html", {
            "form": buyer_form
        })



