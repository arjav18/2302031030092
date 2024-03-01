"""shopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from customer import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('store_register/', views.store_register, name='store_register'),
    path('login/', views.login, name='login'),
    path('login_check/', views.login_check, name='login_check'),    
    path('logout/', views.logout, name='logout'),

    path('home/', views.home, name='home'),
    path('edit_profile/<int:id>', views.edit_profile, name='edit_profile'),
    path('update_profile/<int:id>', views.update_profile, name='update_profile'),
    
    path('offer/', views.offer, name='offer'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('faq/', views.faq, name='faq'),
    path('products/<int:id>', views.products, name='products'),
    path('single/<int:id>', views.single, name='single'),
    path('checkout/', views.checkout, name='checkout'),
    path('shipping/', views.shipping, name='shipping'),
    path('payment/', views.payment, name='payment'),
]
