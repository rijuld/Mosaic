from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.forms import ModelForm
from .models import User,auctionlisting,comments,bid,Categories,watchlist
from django.db.models import Max
from django.contrib.auth.decorators import login_required

class createform(ModelForm):
	class Meta:
		model=auctionlisting
		fields=['title','description','image','startingprice','category']

class addform(ModelForm):
	class Meta:
		model=bid
		fields=['bids']
class commentform(ModelForm):
	class Meta:
		model=comments
		fields=['comment']




def index(request):
	a=auctionlisting.objects.filter(status="ac")
	b=bid.objects.all()
	k={}
	for i in a:
		arg=bid.objects.filter(item=i)
		d=arg.order_by('-bids').first()
		k[i]=d


	return render(request, "auctions/index.html",{
			
			"k":k

		})
@login_required(login_url='login')
def won(request):
	c=[]
	user=request.user
	a=auctionlisting.objects.filter(status="cl")
	for i in a:
		arg=bid.objects.filter(item=i)
		d=arg.order_by('-bids').first()	
		if d.person==user:
			c.append(i)


	return render(request, "auctions/won.html",{
			"list":c
		})
	
		



def login_view(request):
	if request.method == "POST":

		# Attempt to sign user in
		username = request.POST["username"]
		password = request.POST["password"]
		user = authenticate(request, username=username, password=password)

		# Check if authentication successful
		if user is not None:
			login(request, user)
			return HttpResponseRedirect(reverse("auctions:index"))
		else:
			return render(request, "auctions/login.html", {
				"message": "Invalid username and/or password."
			})
	else:
		return render(request, "auctions/login.html")


def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse("auctions:index"))


def register(request):
	if request.method == "POST":
		username = request.POST["username"]
		email = request.POST["email"]

		# Ensure password matches confirmation
		password = request.POST["password"]
		confirmation = request.POST["confirmation"]
		if password != confirmation:
			return render(request, "auctions/register.html", {
				"message": "Passwords must match."
			})

		# Attempt to create new user
		try:
			user = User.objects.create_user(username, email, password)
			user.save()
		except IntegrityError:
			return render(request, "auctions/register.html", {
				"message": "Username already taken."
			})
		login(request, user)
		return HttpResponseRedirect(reverse("auctions:index"))
	else:
		return render(request, "auctions/register.html")
	
def listing(request, title):
	if request.method=="POST":
		form = addform(request.POST)
		if form.is_valid():
			listing=auctionlisting.objects.get(title=title)
			bids = form.cleaned_data["bids"]
			arg=bid.objects.filter(item=listing)
			d=arg.order_by('-bids').first()
			if bids>d.bids:
				person=request.user
				item=auctionlisting.objects.get(title=title)
				f =bid(person=person,item=item,bids=bids)
				f.save()
			else:
				return HttpResponse("<h1>Oops, Your bid is less than the current highest bid,Try again with a higher bid!</h1>")
            
           		
	
	listing=auctionlisting.objects.get(title=title)
	if listing.status=="ac":
		b=comments.objects.filter(item=listing)
		c=commentform()
		user = request.user 
		arg=bid.objects.filter(item=listing)
		d=arg.order_by('-bids').first()
		f=watchlist.objects.all()
		if not f:
			j=0
		for i in f:
			if i.item==listing and i.user==user :
				j=1
			else:
				j=0

		form=addform()
		return render(request,"auctions/listing.html",{
		"listing":listing,
		"form":form,
		"commen":b,
		"commentform":c,
		"d":d,
		"j":j


		


		})
	else:
		user = request.user 
		arg=bid.objects.filter(item=listing)
		d=arg.order_by('-bids').first()
		if d.person==user:
			return render(request,"auctions/youwon.html",{
				"d":d
				})

@login_required(login_url='login')
def watch(request):

	return render(request,"auctions/watchlist.html",{
		"lists":watchlist.objects.all()
		})
@login_required(login_url='login')
def createlisting(request):
	if request.method=="POST":
		form = createform(request.POST)
		if form.is_valid():
			title = form.cleaned_data["title"]
			description = form.cleaned_data["description"]
			image = form.cleaned_data["image"]
			startingprice= form.cleaned_data["startingprice"]
			category = form.cleaned_data["category"]
			name=request.user
			
			f =auctionlisting(title=title,description=description,image=image,name=name,startingprice=startingprice,category=category)
			f.save()
			g=bid(person=request.user,item=f,bids=f.startingprice)
			g.save()
	c=Categories.objects.all()
	form=createform()
	return render(request,"auctions/createlisting.html",{
		"form":form,
		"cat":c
		})

def category(request):
	return render(request,"auctions/category.html",{
		"cat":Categories.objects.all()
		})
@login_required(login_url='login')
def add(request,title):
	if request.method=="POST":
		listing=auctionlisting.objects.get(title=title)
		user = request.user 
		f =watchlist(user=user,item=listing)
		f.save()
		return HttpResponseRedirect(reverse("auctions:listing",kwargs={'title': title}))
@login_required(login_url='login')
def remove(request,title):
	if request.method=="POST":
		listing=auctionlisting.objects.get(title=title)
		user = request.user 
		f =watchlist.objects.get(user=user,item=listing)
		f.delete()
		return HttpResponseRedirect(reverse("auctions:listing",kwargs={'title': title}))

def subcategory(request,title):
	if request.method=="POST":
		form = commentform(request.POST)
		if form.is_valid():
			comment = form.cleaned_data["comment"]
			user=request.user
			item=auctionlisting.objects.get(title=title)
			f =comments(user=user,item=item,comment=comment)
			f.save()
			return HttpResponseRedirect(reverse("auctions:listing",kwargs={'title': title}))
	cate=Categories.objects.get(x=title)
	a=auctionlisting.objects.filter(category=cate)
	return render(request,"auctions/subcategory.html",{
		"cat":a
		})
@login_required(login_url='login')
def mylist(request):
	user = request.user 
	v=auctionlisting.objects.filter(name=user)
	return render(request,"auctions/mylist.html",{
		"v":v
		})
@login_required(login_url='login')
def close(request,title):
	user=request.user
	listing=auctionlisting.objects.get(title=title,name=user)
	v=auctionlisting.objects.filter(name=user)
	listing.status="cl"
	listing.save()
	return render(request,"auctions/mylist.html",{
		"v":v
		})
	









