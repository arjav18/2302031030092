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
from seller import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('dashboard_seller/', views.dashboard_seller, name='dashboard_seller'),
    path('login_check_shopping/', views.login_check_shopping, name='login_check_shopping'),
    path('home_login/', views.home_login, name='home_login'),
    path('login_seller_shopping/', views.login_seller_shopping, name='login_seller_shopping'),
    path('logout/', views.logout, name='logout'),

    path('create_product/', views.create_product, name='create_product'),
    path('store_product/',views.store_product,name='store_product'),
    path('read_product/', views.read_product, name='read_product'),
    path('delete_product/<int:id>',views.delete_product,name='delete_product'),
    path('edit_product_/<int:id>',views.edit_product,name='edit_product'),
    path('update_product/<int:id>',views.update_product,name='update_product'),

    
]
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)