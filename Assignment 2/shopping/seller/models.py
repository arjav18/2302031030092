from django.db import models
from myadmin.models import Category,SubCategory

# Create your models here.

class Product(models.Model):
    pname=models.CharField(max_length=50, default=None)
    price=models.BigIntegerField(default=None)
    sdesc=models.TextField(default=None)
    ldesc=models.TextField(default=None)
    category=models.ForeignKey(Category,on_delete=models.CASCADE, default=None)
    subcategory=models.ForeignKey(SubCategory,on_delete=models.CASCADE, default=None)
    file_name=models.FileField(max_length=255, default=None)

    class Meta:
        db_table='product'