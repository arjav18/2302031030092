from multiprocessing import context
from unicodedata import category
from unittest import result
from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from customer.models import registeration
from django.contrib import auth, messages
from myadmin.models import Seller, State, City, Category,SubCategory
from seller.models import Product


# login-register

def register(request):
    statez = State.objects.all()
    cityz = City.objects.all()
    context={'states':statez,'cities':cityz} 
    
    return render(request, 'customer/register.html', context)

def store_register(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    cpassword = request.POST['cpassword']

    # Model: Profile
    contact = request.POST['contact']
    address = request.POST['address']
    mystate = request.POST['state']
    mycity = request.POST['city']
    if password == cpassword:
        User.objects.create_user(first_name=fname, last_name=lname, email=email, username=username, password=password)
        registeration.objects.create(contact=contact, address=address, state_id=mystate, city_id=mycity, user_id=User.id)

        return redirect('/customer/home/')
    else:
        messages.error(request, "Password Mismatched")
        return redirect('/customer/register/')

def login(request):
    context = {}
    return render(request, 'customer/login.html', context)

def login_check(request):
    myusername = request.POST['username']
    mypassword = request.POST['password']

    result = auth.authenticate(username=myusername, password=mypassword)

    if result is None:
        messages.error(request, 'Invalid Username or Password')
        return redirect('/customer/login/')
    else:
        auth.login(request,result)
        return redirect('/customer/home/')
        
def logout(request):
	auth.logout(request)
	return redirect('/customer/home/')

# navigation


def home(request):
    result=Category.objects.all()
    result1=SubCategory.objects.all()
    context = {'categories':result,'subcategories':result1}
    return render(request, 'customer/home.html', context)

def edit_profile(request, id):
    result = registeration.objects.get(pk=id)
    context={'result':result}
    return render(request, 'customer/edit_profile.html', context)

def update_profile(request,id):
    fname=request.POST['fname']
    lname=request.POST['lname']
    email=request.POST['email']    
    contact=request.POST['contact']
    mystate = request.POST['state']
    mycity = request.POST['city']
    address=request.POST['address']
    username=request.POST['username']
    password=request.POST['password']

    data={
        'first_name':fname,
        'last_name':lname,
        'email':email,
        'contact':contact,
        'state_id':mystate,
        'city_id':mycity,
        'address':address,
        'username':username,
        'password':password,
    }
    registeration.objects.update_or_create(defaults=data,user_id=id)
    return redirect('/customer/edit_profile/')

def offer(request):
    result=Category.objects.all()
    result1=SubCategory.objects.all()
    context = {'categories':result,'subcategories':result1}
    
    return render(request, 'customer/offer.html', context)

def contact(request):
    result=Category.objects.all()
    result1=SubCategory.objects.all()
    context = {'categories':result,'subcategories':result1}
    
    return render(request, 'customer/contact.html', context)

def about(request):
    result=Category.objects.all()
    result1=SubCategory.objects.all()
    context = {'categories':result,'subcategories':result1}
    
    return render(request, 'customer/about.html', context)

def faq(request):
    result=Category.objects.all()
    result1=SubCategory.objects.all()
    context = {'categories':result,'subcategories':result1}
    
    return render(request, 'customer/faq.html', context)

def products(request,id):
    result=Category.objects.all()
    result1=SubCategory.objects.all()
    products = Product.objects.filter(subcategory_id=id)
    context = {'categories':result,'subcategories':result1,'products':products}
    return render(request, 'customer/product.html', context)

def single(request,id):
    result=Category.objects.all()
    result1=SubCategory.objects.all()
    productz=Product.objects.get(pk=id)
    context = {'categories':result,'subcategories':result1,'prod':productz}
    
    
    return render(request, 'customer/single.html', context)

def checkout(request):
    result=Category.objects.all()
    result1=SubCategory.objects.all()
    context = {'categories':result,'subcategories':result1}
    return render(request, 'customer/checkout.html', context)

def shipping(request):
    result=Category.objects.all()
    result1=SubCategory.objects.all()
    statez = State.objects.all()
    cityz = City.objects.all()
    context={'categories':result,'subcategories':result1, 'states':statez,'cities':cityz} 
    
    return render(request, 'customer/shipping.html', context)

def store_shipping(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    username = request.POST['username']
    email = request.POST['email']

    # Model: Profile
    contact = request.POST['contact']
    address = request.POST['address']
    mystate = request.POST['state']
    mycity = request.POST['city']


def payment(request):
    result=Category.objects.all()
    result1=SubCategory.objects.all()
    context = {'categories':result,'subcategories':result1}
    
    return render(request, 'customer/payment.html', context)