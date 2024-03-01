"""hifix URL Configuration

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
from django.urls import path,include
from myadmin import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('dashboard_shopping/', views.dashboard_shopping, name='dashboard_shopping'),
    path('login_check_shopping/', views.login_check_shopping, name='login_check_shopping'),
    path('home_login/', views.home_login, name='home_login'),
    path('login_admin_shopping/', views.login_admin_shopping, name='login_admin_shopping'),
    path('logout/', views.logout, name='logout'),

    path('create_state_shopping/', views.create_state_shopping, name='create_state_shopping'),
    path('store_state_shopping/', views.store_state_shopping, name='store_state_shopping'),
    path('read_state_shopping/', views.read_state_shopping, name='read_state_shopping'),
    path('delete_state_shopping/<int:id>', views.store_state_shopping, name='store_state_shopping'),
    path('edit_state_shopping/<int:id>',views.edit_state_shopping,name='edit_state_shopping'),
    path('update_state_shopping/<int:id>',views.update_state_shopping,name='update_state_shopping'),

    path('create_city_shopping/', views.create_city_shopping, name='create_city_shopping'),
    path('store_city_shopping/',views.store_city_shopping,name='store_city_shopping'),
    path('read_city_shopping/',views.read_city_shopping,name='read_city_shopping'),
    path('delete_city_shopping/<int:id>',views.delete_city_shopping,name='delete_city_shopping'),
    path('edit_city_shopping/<int:id>',views.edit_city_shopping,name='edit_city_shopping'),
    path('update_city_shopping/<int:id>',views.update_city_shopping,name='update_city_shopping'),

    path('create_category_shopping/', views.create_category_shopping, name='create_category_shopping'),
    path('store_category_shopping/',views.store_category_shopping,name='store_category_shopping'),
    path('read_category_shopping/', views.read_category_shopping, name='read_category_shopping'),
    path('delete_category_shopping/<int:id>',views.delete_category_shopping,name='delete_category_shopping'),
    path('edit_category_shopping/<int:id>',views.edit_category_shopping,name='edit_category_shopping'),
    path('update_category_shopping/<int:id>',views.update_category_shopping,name='update_category_shopping'),

    path('create_subcategory_shopping/', views.create_subcategory_shopping, name='create_subcategory_shopping'),
    path('store_subcategory_shopping/',views.store_subcategory_shopping,name='store_subcategory_shopping'),
    path('read_subcategory_shopping/', views.read_subcategory_shopping, name='read_subcategory_shopping'),
    path('delete_subcategory_shopping/<int:id>',views.delete_subcategory_shopping,name='delete_subcategory_shopping'),
    path('edit_subcategory_shopping/<int:id>',views.edit_subcategory_shopping,name='edit_subcategory_shopping'),
    path('update_subcategory_shopping/<int:id>',views.update_subcategory_shopping,name='update_subcategory_shopping'),

    path('create_seller_shopping/', views.create_seller_shopping, name='create_seller_shopping'),
    path('store_seller_shopping/',views.store_seller_shopping,name='store_seller_shopping'),
    path('read_seller_shopping/',views.read_seller_shopping,name='read_seller_shopping'),
     path('delete_subcategory_shopping/<int:id>',views.delete_subcategory_shopping,name='delete_subcategory_shopping'),
    path('edit_seller_shopping/<int:id>',views.edit_seller_shopping,name='edit_seller_shopping'),
    path('update_seller_shopping/<int:id>',views.update_seller_shopping,name='update_seller_shopping'),

    
]
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)