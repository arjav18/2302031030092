from django.db import models
from django.contrib.auth.models import User

class Seller(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,default=None)
    contact=models.BigIntegerField(default=None)
    address=models.TextField(default=None)    

    class Meta:
        db_table='seller'

class State(models.Model):
    state=models.CharField(max_length=50)

    class Meta:
        db_table='state'

class City(models.Model):
    city=models.CharField(max_length=40)
    state=models.ForeignKey(State, on_delete=models.CASCADE)
    
    class Meta:
        db_table='city'

class Category(models.Model):
    category=models.CharField(max_length=50)

    class Meta:
        db_table='category'

class SubCategory(models.Model):
    subcategory=models.CharField(max_length=60)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    class Meta:
        db_table='subcategory'