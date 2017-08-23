from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime

# Create your models here.
#products model with product information
class Product(models.Model):
    product_name = models.CharField(max_length=70)
    style = models.CharField(max_length=70)
    price = models.FloatField()
    type = models.CharField(max_length=15)
    color = models.CharField(max_length=15)
    favorite = models.BooleanField()
    display_rank = models.IntegerField()
    image_url = models.CharField(default='images/image', max_length=70)

    def __str__(self):
        return self.product_name

#user model with user information
#class Customer(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE, default="")
    #location = models.CharField(max_length=30, default="USA")

    #def __str__(self):
        #return u'%s %s' % (self.user.first_name, self.user.last_name)

#orcers model, links by foreign key with relvant products and customers
class Order(models.Model):
    date = models.DateTimeField('date ordered')
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)

    def __str__(self):
        return str(self.id)

#model for messages and correspondance
class Messages(models.Model):
    date = models.DateTimeField(default=timezone.now())
    #customer = models.ForeignKey(Customer)
    text =  models.TextField()
    email = models.EmailField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


    def __str__(self):
        return str(self.id)

