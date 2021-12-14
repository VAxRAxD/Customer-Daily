from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
	user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	address=models.CharField(max_length=500,null=True)
	profile_pic = models.ImageField(default="profile.png", null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name


class Product(models.Model):
	CATEGORY = (
			('Chicken', 'Chicken'),
			('Mutton', 'Mutton'),
			('Seafood', 'Seafood'),
			) 

	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	weight=models.CharField(max_length=200,null=True)
	description = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name

class Order(models.Model):
	STATUS = (
			('Pending', 'Pending'),
			('Out for delivery', 'Out for delivery'),
			('Delivered', 'Delivered'),
			)
	customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
	product=models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS,default="Pending")
	quantity=models.IntegerField(null=False,default=1)

	def __str__(self):
		return self.product.name