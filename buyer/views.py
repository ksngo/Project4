from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Buyer
from .forms import BuyerForm
from vendor.models import Vendor
from food.models import Food
from order.models import OrderLineItem
# Create your views here.


def view_home(request):

    no_of_vendors = Vendor.objects.count()

    no_of_vendors_amk = Vendor.objects.filter(vendordeliverytown__town="ANG MO KIO").count()
    no_of_vendors_bedok = Vendor.objects.filter(vendordeliverytown__town="BEDOK").count()
    no_of_vendors_bishan = Vendor.objects.filter(vendordeliverytown__town="BISHAN").count()
    no_of_vendors_batok = Vendor.objects.filter(vendordeliverytown__town="BUKIT BATOK").count()
    no_of_vendors_merah = Vendor.objects.filter(vendordeliverytown__town="BUKIT MERAH").count()
    no_of_vendors_panjang = Vendor.objects.filter(vendordeliverytown__town="BUKIT PANJANG").count()
    no_of_vendors_timah = Vendor.objects.filter(vendordeliverytown__town="BUKIT TIMAH").count()
    no_of_vendors_central = Vendor.objects.filter(vendordeliverytown__town="CENTRAL AREA").count()
    no_of_vendors_cck = Vendor.objects.filter(vendordeliverytown__town="CHOA CHU KANG").count()
    no_of_vendors_clementi = Vendor.objects.filter(vendordeliverytown__town="CLEMENTI").count()
    no_of_vendors_geylang = Vendor.objects.filter(vendordeliverytown__town="GEYLANG").count()
    no_of_vendors_hougang = Vendor.objects.filter(vendordeliverytown__town="HOUGANG").count()
    no_of_vendors_jurongeast = Vendor.objects.filter(vendordeliverytown__town="JURONG EAST").count()
    no_of_vendors_jurongwest = Vendor.objects.filter(vendordeliverytown__town="JURONG WEST").count()
    no_of_vendors_kw = Vendor.objects.filter(vendordeliverytown__town="KALLANG/WHAMPOA").count()
    no_of_vendors_mp = Vendor.objects.filter(vendordeliverytown__town="MARINE PARADE").count()
    no_of_vendors_pasir = Vendor.objects.filter(vendordeliverytown__town="PASIR RIS").count()
    no_of_vendors_punggol = Vendor.objects.filter(vendordeliverytown__town="PUNGGOL").count()
    no_of_vendors_qt = Vendor.objects.filter(vendordeliverytown__town="QUEENSTOWN").count()
    no_of_vendors_sembawang = Vendor.objects.filter(vendordeliverytown__town="SEMBAWANG").count()
    no_of_vendors_sengkang = Vendor.objects.filter(vendordeliverytown__town="SENGKANG").count()
    no_of_vendors_serangoon = Vendor.objects.filter(vendordeliverytown__town="SERANGOON").count()
    no_of_vendors_tampines = Vendor.objects.filter(vendordeliverytown__town="TAMPINES").count()
    no_of_vendors_toapayoh = Vendor.objects.filter(vendordeliverytown__town="TOA PAYOH").count()
    no_of_vendors_woodlands = Vendor.objects.filter(vendordeliverytown__town="WOODLANDS").count()
    no_of_vendors_yishun = Vendor.objects.filter(vendordeliverytown__town="YISHUN").count()

    return render(request, "buyer/home.html", {
        "no_of_vendors": no_of_vendors,
        "no_of_vendors_amk": no_of_vendors_amk,
        "no_of_vendors_bedok": no_of_vendors_bedok,
        "no_of_vendors_bishan": no_of_vendors_bishan,
        "no_of_vendors_batok": no_of_vendors_batok,
        "no_of_vendors_merah": no_of_vendors_merah,
        "no_of_vendors_panjang": no_of_vendors_panjang,
        "no_of_vendors_timah": no_of_vendors_timah,
        "no_of_vendors_central": no_of_vendors_central,
        "no_of_vendors_cck": no_of_vendors_cck,
        "no_of_vendors_clementi": no_of_vendors_clementi,
        "no_of_vendors_geylang": no_of_vendors_geylang,
        "no_of_vendors_hougang": no_of_vendors_hougang,
        "no_of_vendors_jurongeast": no_of_vendors_jurongeast,
        "no_of_vendors_jurongwest": no_of_vendors_jurongwest,
        "no_of_vendors_kw": no_of_vendors_kw,
        "no_of_vendors_mp": no_of_vendors_mp,
        "no_of_vendors_pasir": no_of_vendors_pasir,
        "no_of_vendors_punggol": no_of_vendors_punggol,
        "no_of_vendors_qt": no_of_vendors_qt,
        "no_of_vendors_sembawang": no_of_vendors_sembawang,
        "no_of_vendors_sengkang": no_of_vendors_sengkang,
        "no_of_vendors_serangoon": no_of_vendors_serangoon,
        "no_of_vendors_tampines": no_of_vendors_tampines,
        "no_of_vendors_toapayoh": no_of_vendors_toapayoh,
        "no_of_vendors_woodlands": no_of_vendors_woodlands,
        "no_of_vendors_yishun": no_of_vendors_yishun,

    })




@login_required
def create_buyer_profile(request):
    buyer_form = BuyerForm()

    if request.method == "POST":
        buyer_form = BuyerForm(request.POST)

        if buyer_form.is_valid():
            form = buyer_form.save(commit=False)
            form.user = request.user
            form.save()
            messages.success(request, "New Profile added.")
            return redirect(reverse(show_buyer_profiles))
        else:
            messages.warning(request, "Contact field must be 8 digits number.")
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

        if buyer_form.is_valid():

            buyer_form.save()  # does not require to commit False form to save user as request.user; user still intact in database after the save

            messages.success(request, "Profile successfully updated.")
            return redirect(reverse(show_buyer_profiles))

        else:
            messages.warning(request, "Contact field must be 8 digits number.")
            return redirect(reverse(edit_buyer_profile, kwargs={"buyer_id": buyer_id}))

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
        messages.success(request, f" Profile '{buyer_profile}' deleted ")
        buyer_profile.delete()
        return redirect(reverse(show_buyer_profiles))

    else:

        return render(request, "buyer/delete_buyer_profile.html", {
            "object": buyer_profile
        })

@login_required
def index(request):

    buyer_profiles = Buyer.objects.all().filter(user=request.user)
    default_buyer_object = Buyer.objects.all().filter(user=request.user)[:1]

    for i in default_buyer_object:
        default_buyer_id = i.id

    if buyer_profiles:

        buyer_town = Buyer.objects.get(id=default_buyer_id).town.upper()
        buyer_postal = Buyer.objects.get(id=default_buyer_id).postal_code

        vendor_available_base_queries = Q(vendordeliverytown__town=buyer_town) | Q(vendordeliverypostal__postal_code__exact=buyer_postal)
        food_available_base_queries = Q(vendor__vendordeliverytown__town=buyer_town) | Q(vendor__vendordeliverypostal__postal_code__exact=buyer_postal)

        vendor_available = Vendor.objects.filter(vendor_available_base_queries).distinct()

        food_available = Food.objects.filter(food_available_base_queries).distinct()

    else:

        buyer_profiles = False
        vendor_available = False
        food_available = False
        default_buyer_id = False

    return render(request, 'buyer/buyer_index_page.html', {
        "buyer_profiles": buyer_profiles,
        "vendor_available": vendor_available,
        "food_available": food_available,
        "buyer_id": default_buyer_id
    })


@login_required
def index_by_profile(request, buyer_id):

    buyer_profiles = Buyer.objects.all().filter(user=request.user)  # retrieve all buyer profiles for user

    buyer_town = Buyer.objects.get(id=buyer_id).town.upper()  # retrieve buyer profile's town
    buyer_postal = Buyer.objects.get(id=buyer_id).postal_code  # retrieve buyer profile's postal code

    vendor_available_base_queries = Q(vendordeliverytown__town=buyer_town)|Q(vendordeliverypostal__postal_code__exact=buyer_postal)
    food_available_base_queries = Q(vendor__vendordeliverytown__town=buyer_town)|Q(vendor__vendordeliverypostal__postal_code__exact=buyer_postal)

    if 'category' in request.GET:

        get_category = request.GET['category']

        vendor_available = Vendor.objects.filter(vendor_available_base_queries).filter(category__title=get_category).distinct()

        food_available = Food.objects.filter(food_available_base_queries).filter(vendor__category__title=get_category).distinct()

    elif 'tag' in request.GET:

        get_tag = request.GET['tag']

        # cant reverse in filter() to query on Vendor to Food as vendor is a foreign key in Food table only.
        # Hence, first filter on Food table to the tags(which is a m2m field in Food table).
        # Then, find out the vendors id(vendor is foreign key in Food table) by looping through above filter queryset result and save into a list.
        # Then, filter on Vendor table to the list of vendors id using filter(id__in=[list])

        get_foods_with_tag = Food.objects.filter(tag__title=get_tag)
        vendors_list = []
        for i in get_foods_with_tag:
            vendors_list.append(i.vendor.id)

        vendor_available = Vendor.objects.filter(vendor_available_base_queries).filter(id__in=vendors_list).distinct()

        # this is not possible because Vendor.objects.fitler() returns a queryset; *_set work with Vendor.objects.get() which returns an object
        # vendor_available = Vendor.objects.filter(
        #         vendordeliverytown__town=buyer_town
        #     ).food_set.filter(
        #         tag__title=get_tag
        #     )

        food_available = Food.objects.filter(food_available_base_queries).filter(tag__title=get_tag).distinct()

    elif 'search' in request.GET:

        query = request.GET['search']

        if not query:
            messages.error(request, "You have not enter a search term.")
            return redirect(reverse(index))

        vendor_queries = Q(name__icontains=query)
        vendor_available = Vendor.objects.filter(vendor_available_base_queries).filter(vendor_queries).distinct()

        food_queries = Q(title__icontains=query) | Q(description__icontains=query)
        food_available = Food.objects.filter(food_available_base_queries).filter(food_queries).distinct()

        if vendor_available and not food_available:
            print("inside vendor queries and not food queries")

            vendor_id_list = []
            for i in vendor_available:
                vendor_id_list.append(i.id)
                print(vendor_id_list)
            # overide above food_available since it's empty too.
            food_available = Food.objects.filter(food_available_base_queries).filter(vendor__id__in=vendor_id_list).distinct()

        elif food_available and not vendor_available:
            print("inside food queries and not vendor queries")
            vendor_id_list = []
            for i in food_available:
                vendor_id_list.append(i.vendor.id)

            vendor_available = Vendor.objects.filter(vendor_available_base_queries).filter(id__in=vendor_id_list).distinct()

    else:

        vendor_available = Vendor.objects.filter(vendor_available_base_queries).distinct()  # retrieve vendors that deliver to buyer profile's town and postal

        food_available = Food.objects.filter(food_available_base_queries).distinct()  # retrieve foods that can be delivered to buyer profiles town and postal

    return render(request, 'buyer/buyer_index_page.html', {
        "buyer_profiles": buyer_profiles,
        "vendor_available": vendor_available,
        "food_available": food_available,
        "buyer_id": buyer_id
    })


@login_required
def view_order_history(request):

    orders = OrderLineItem.objects.all().filter(order__user=request.user)

    return render(request, "buyer/buyer_order_history.html", {
        "orders": orders
    })