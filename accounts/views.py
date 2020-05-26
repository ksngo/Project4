from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def view_account(request):

    user_email = request.user.email
    user_name = request.user.username
    

    return render(request, "accounts/account.html", {
        "user_email":user_email,
        "user_name": user_name
    })