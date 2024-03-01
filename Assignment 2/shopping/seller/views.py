from unittest import result
from django.shortcuts import render,redirect
from django.contrib import auth,messages
from myadmin.models import SubCategory,Category
from seller.models import Product
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

def dashboard_seller(request):
	context={}
	return render(request,'seller/dashboard_seller.html',context)

def login_seller_shopping(request):
    context={}
    return render(request,'seller/login_seller.html',context)

def home_login(request):
    # id=request.user.id
    # result=User.objects.get(pk=id)
    context={}
    return render(request,'seller/dashboard_seller.html',context)


def login_check_shopping(request):
    myusername = request.POST['username']
    mypassword = request.POST['password']

    result = auth.authenticate(username=myusername, password=mypassword)

    if result is None:
        messages.error(request, 'Invalid Username or Password')
        return redirect('/seller/login_seller_shopping/')
    else:
        # auth.login(request,result)
        return redirect('/seller/dashboard_seller/')


def logout(request):
	auth.logout(request)
	return redirect('/seller/login_seller_shopping/')
    

def create_product(request):
	result=Category.objects.all()
	result1=SubCategory.objects.all()
	context={'categories':result,'subcategories':result1}
	return render(request,'seller/create_product.html',context)

def store_product(request):
	pname=request.POST['pname']
	price=request.POST['price']
	sdesc=request.POST['sdesc']
	ldesc=request.POST['ldesc']
	category=request.POST['category']
	subcategory=request.POST['subcategory']
	myfile=request.FILES.get('image')

	mylocation = os.path.join(settings.MEDIA_ROOT,'upload')
	obj = FileSystemStorage(location= mylocation)
	obj.save(myfile.name,myfile)

	Product.objects.create(pname=pname,price=price,sdesc=sdesc,ldesc=ldesc,category_id=category,subcategory_id=subcategory,file_name=myfile.name)

	return redirect('/seller/create_product/')

def read_product(request):
	result = Product.objects.all()
	context = {'result':result}

	return render (request, 'seller/read_product.html', context)


def delete_product(request,id):
	result=Product.objects.get(pk=id)	
	result.delete()

	return redirect('/seller/read_product/')

def edit_product(request,id):
	result1=Category.objects.all()
	result2=SubCategory.objects.all()
	result=Product.objects.get(pk=id)

	context={'categories':result1,'subcategories':result2,'result':result}
	return render(request,'seller/edit_product_shopping.html',context)

def update_product(request,id):

	pname=request.POST['pname']
	price=request.POST['price']
	sdesc=request.POST['sdesc']
	ldesc=request.POST['ldesc']
	category=request.POST['category']
	subcategory=request.POST['subcategory']
	myfile=request.FILES.get('image')

	mylocation = os.path.join(settings.MEDIA_ROOT,'upload')
	obj = FileSystemStorage(location= mylocation)
	obj.save(myfile.name,myfile)

	data={
		'pname':pname,
		'price':price,
		'sdesc':sdesc,
		'ldesc':ldesc,
		'category_id':category,
		'subcategory_id':subcategory
	}

	Product.objects.update_or_create(defaults=data,pk=id)
	return redirect('/seller/read_product/')