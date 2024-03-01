from contextlib import ContextDecorator
from django.db import models
from myadmin.models import State, City
from django.contrib.auth.models import User

class registeration(models.Model):
    user =  models.OneToOneField(User, on_delete = models.CASCADE, default=None)
    contact = models.BigIntegerField(default=None)
    state= models.ForeignKey(State, on_delete = models.CASCADE, default=None)
    city = models.ForeignKey(City, on_delete = models.CASCADE, default=None)
    address = models.TextField(default=None)

    class Meta:
        db_table = 'register'