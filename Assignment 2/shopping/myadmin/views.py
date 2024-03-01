from django.shortcuts import render
from multiprocessing import context
from unicodedata import category
from unittest import result
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
from myadmin.models import State, City, Category, SubCategory, Seller, User

# Create your views here.
def dashboard_shopping(request):
    context = {}
    return render(request, "myadmin/dashboard_shopping.html", context)


def login_admin_shopping(request):
    context = {}
    return render(request, "myadmin/login_admin_shopping.html", context)


def home_login(request):
    context = {}
    return render(request, "myadmin/dashboard_shopping.html", context)


def login_check_shopping(request):
    myusername = request.POST["username"]
    mypassword = request.POST["password"]

    result = auth.authenticate(username=myusername, password=mypassword)

    if result is None:
        messages.error(request, "Invalid Username or Password")
        return redirect("/myadmin/login_admin_shopping/")
    else:
        # auth.login(request,result)
        return redirect("/myadmin/dashboard_shopping/")


def logout(request):
    auth.logout(request)
    return redirect("/myadmin/login_admin_shopping/")


# Crud for state


def create_state_shopping(request):
    context = {}
    return render(request, "myadmin/create_state_shopping.html", context)


def store_state_shopping(request):
    mystate = request.POST["state"]

    if State.objects.filter(state=mystate).exists():
        messages.error(request, "State already registered!")
        return redirect("/myadmin/create_state_shopping/")

    State.objects.create(state=mystate)

    return redirect("/myadmin/create_state_shopping/")


def read_state_shopping(request):
    result = State.objects.all()
    context = {"result": result}

    return render(request, "myadmin/read_state_shopping.html", context)


def delete_state_shopping(request, id):
    result = State.objects.get(pk=id)
    result.delete()
    return redirect("/myadmin/read_state_shopping/")


def edit_state_shopping(request, id):
    result = State.objects.get(pk=id)
    context = {"result": result}

    return render(request, "myadmin/edit_state_shopping.html", context)


def update_state_shopping(request, id):
    mystate = request.POST["state"]
    data = {"state": mystate}
    if State.objects.filter(state=mystate).exists():
        messages.error(
            request, "State already registered! Kindly Register the New Category First"
        )
        return redirect("/myadmin/create_state_shopping/")
    else:
        State.objects.update_or_create(defaults=data, pk=id)
        return redirect("/myadmin/read_state_shopping/")


# Crud for city


def create_city_shopping(request):
    result = State.objects.all()
    context = {"states": result}

    return render(request, "myadmin/create_city_shopping.html", context)


def store_city_shopping(request):
    mycity = request.POST["city"]
    mystate = request.POST["state"]
    if City.objects.filter(city=mycity).exists():
        messages.error(request, "City already registered!")
        return redirect("/myadmin/create_city_shopping/")

    City.objects.create(state_id=mystate, city=mycity)

    return redirect("/myadmin/create_city_shopping/")


def read_city_shopping(request):
    result = City.objects.all()
    context = {"result": result}

    return render(request, "myadmin/read_city_shopping.html", context)


def delete_city_shopping(request, id):
    result = City.objects.get(pk=id)
    result.delete()

    return redirect("/myadmin/read_city_shopping/")


def edit_city_shopping(request, id):
    result1 = State.objects.all()
    result = City.objects.get(pk=id)
    context = {"result": result, "states": result1}

    return render(request, "myadmin/edit_city_shopping.html", context)


def update_city_shopping(request, id):
    mycity = request.POST["city"]
    mystate = request.POST["state"]
    data = {"state_id": mystate, "city": mycity}
    if City.objects.filter(city=mycity).exists():
        messages.error(
            request, "CIty already registered! Kindly Register the New Category First"
        )
        return redirect("/myadmin/create_city_shopping/")
    else:
        City.objects.update_or_create(defaults=data, pk=id)
        return redirect("/myadmin/read_city_shopping/")


# Crud for Category


def create_category_shopping(request):
    context = {}
    return render(request, "myadmin/create_category.html", context)


def store_category_shopping(request):
    mycategory = request.POST["category"]

    Category.objects.create(category=mycategory)

    return redirect("/myadmin/create_category_shopping/")


def read_category_shopping(request):
    result = Category.objects.all()
    context = {"result": result}

    return render(request, "myadmin/read_category.html", context)


def delete_category_shopping(request, id):
    result = Category.objects.get(pk=id)
    result.delete()

    return redirect("/myadmin/read_category_shopping/")


def edit_category_shopping(request, id):
    result = Category.objects.get(pk=id)
    context = {"result": result}

    return render(request, "myadmin/edit_category.html", context)


def update_category_shopping(request, id):
    mycategory = request.POST["category"]
    data = {"category": mycategory}
    if Category.objects.filter(category=mycategory).exists():
        messages.error(
            request,
            "Category already registered! Kindly Register the New Category First",
        )
        return redirect("/myadmin/create_category_shopping/")
    else:
        Category.objects.update_or_create(defaults=data, pk=id)
        return redirect("/myadmin/read_category_shopping/")


# Crud for Subcategory


def create_subcategory_shopping(request):
    result = Category.objects.all()
    context = {"sub": result}

    return render(request, "myadmin/create_subcategory.html", context)


def store_subcategory_shopping(request):
    mycategory = request.POST["category"]
    mysubcategory = request.POST["subcategory"]

    SubCategory.objects.create(category_id=mycategory, subcategory=mysubcategory)

    return redirect("/myadmin/create_subcategory_shopping/")


def read_subcategory_shopping(request):
    result = SubCategory.objects.all()
    context = {"result": result}

    return render(request, "myadmin/read_subcategory.html", context)


def delete_subcategory_shopping(request, id):
    result = SubCategory.objects.get(pk=id)
    result.delete()

    return redirect("/myadmin/read_subcategory_shopping/")


def edit_subcategory_shopping(request, id):
    result1 = Category.objects.all()
    result = SubCategory.objects.get(pk=id)
    context = {"result": result, "cat": result1}

    return render(request, "myadmin/edit_subcategory.html", context)


def update_subcategory_shopping(request, id):
    mycategory = request.POST["category"]
    subcategory = request.POST["subcategory"]
    data = {"category_id": mycategory, "subcategory": subcategory}
    if SubCategory.objects.filter(subcategory=subcategory).exists():
        messages.error(
            request,
            "SubCategory already registered! Kindly Register the New Category First",
        )
        return redirect("/myadmin/create_subcategory_shopping/")
    else:
        SubCategory.objects.update_or_create(defaults=data, pk=id)
        return redirect("/myadmin/read_subcategory_shopping/")

    # crud for product

    pname = request.POST["pname"]
    price = request.POST["price"]
    sdesc = request.POST["sdesc"]
    ldesc = request.POST["ldesc"]
    category = request.POST["category"]
    subcategory = request.POST["subcategory"]
    myfile = request.FILES.get("image")

    mylocation = os.path.join(settings.MEDIA_ROOT, "upload")
    obj = FileSystemStorage(location=mylocation)
    obj.save(myfile.name, myfile)

    data = {
        "pname": pname,
        "price": price,
        "sdesc": sdesc,
        "ldesc": ldesc,
        "category_id": category,
        "subcategory_id": subcategory,
    }

    Product.objects.update_or_create(defaults=data, pk=id)
    return redirect("/myadmin/read_product_shopping/")


def create_seller_shopping(request):
    result1 = State.objects.all()
    result2 = City.objects.all()
    context = {"states": result1, "cities": result2}
    return render(request, "myadmin/create_seller_shopping.html", context)


def store_seller_shopping(request):
    fname = request.POST["fname"]
    lname = request.POST["lname"]
    username = request.POST["username"]
    email = request.POST["email"]
    password = request.POST["password"]
    cpassword = request.POST["cpassword"]
    contact = request.POST["contact"]
    address = request.POST["address"]

    if password == cpassword:
        user = User.objects.create_user(
            first_name=fname,
            last_name=lname,
            email=email,
            username=username,
            password=password,
        )
        Seller.objects.create(contact=contact, address=address, user_id=user.id)
        return redirect("/myadmin/create_seller_shopping/")

    else:
        print("Password and Confirm Password doesnot match")
        return redirect("/myadmin/create_seller_shopping/")


def read_seller_shopping(request):
    result = Seller.objects.all()
    context = {"result": result}
    return render(request, "myadmin/read_seller_shopping.html", context)


def delete_seller_shopping(request, id):
    result = Seller.objects.get(pk=id)
    result.delete()
    return redirect("/myadmin/read_seller_shopping/")


def edit_seller_shopping(request, id):
    result = Seller.objects.get(pk=id)
    context = {"result": result}
    return render(request, "myadmin/edit_seller_shopping.html", context)


def update_seller_shopping(request, id):
    fname = request.POST["fname"]
    lname = request.POST["lname"]
    username = request.POST["username"]
    email = request.POST["email"]
    password = request.POST["password"]
    contact = request.POST["contact"]
    address = request.POST["address"]

    data = {
        "first_name": fname,
        "last_name": lname,
        "username": username,
        "email": email,
        "password": password,
        "contact": contact,
        "address": address,
    }
    Seller.objects.update_or_create(defaults=data, pk=id)
    return redirect("/myadmin/read_seller_shopping/")
