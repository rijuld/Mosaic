from django.contrib.auth.models import AbstractUser
from django.db import models
class User(AbstractUser):
	pass
class Categories(models.Model):
	x=models.CharField(max_length=64)

class auctionlisting(models.Model):
	active='ac'
	closed='cl'
	Lm = [
    (active, 'active'),
    (closed, 'closed')
	]
	title=models.CharField(max_length=64)
	description=models.CharField(max_length=244)
	image= models.URLField(max_length=200)
	startingprice=models.DecimalField(default=0,max_digits=10, decimal_places=2)
	category=models.ForeignKey(Categories,on_delete=models.CASCADE,related_name="category")
	name=models.ForeignKey(User, on_delete=models.CASCADE,related_name="name")
	status=models.CharField(
        max_length=2,
        choices=Lm,
        default=active,
    )


class comments(models.Model):
	comment=models.CharField(max_length=128)
	item=models.ForeignKey(auctionlisting,on_delete=models.CASCADE,related_name="listing")
	user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user")
class bid(models.Model):
	bids=models.DecimalField(default=0,max_digits=10, decimal_places=2)
	item=models.ForeignKey(auctionlisting,on_delete=models.CASCADE,related_name="thing")
	person=models.ForeignKey(User,on_delete=models.CASCADE,related_name="person")
class watchlist(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="man")
	item=models.ForeignKey(auctionlisting,on_delete=models.CASCADE,related_name="item",primary_key=True)


    


	
