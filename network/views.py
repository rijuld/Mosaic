from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import json
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import following,comments,posts,Todo_likes
from auctions.models import User
from django.http import JsonResponse
from django.core.paginator import Paginator

##################################################################################################################################
def index(request):
    poss=posts.objects.all()
    poss = poss.order_by("-timestamp").all()
    paginator = Paginator(poss, 4)
    try:    
        page_number = request.GET.get('page')
    except Exception as e:
        print(e)
        page_number = 1
    page_obj = paginator.get_page(page_number)
    return render(request, "network/index.html",{'page_obj': page_obj})

##################################################################################################################################
@login_required
def follow(request):
    v=following.objects.filter(user=request.user)
    c=v.values_list('people', flat=True)
    a=posts.objects.filter(sender__in=c)
    poss = a.order_by("-timestamp").all()
    paginator = Paginator(poss, 4)
   
    try:    
        page_number = request.GET.get('page')
    except Exception as e:
        print(e)
        page_number = 1
    page_obj = paginator.get_page(page_number)

    return render(request, "network/follow.html",{
            'page_obj': page_obj
            
    })

##################################################################################################################################
@login_required
def mypage(request):
    a=posts.objects.filter(sender=request.user)
    poss = a.order_by("-timestamp").all()
    paginator = Paginator(poss, 4)
    try:    
        page_number = request.GET.get('page')
    except Exception as e:
        print(e)
        page_number = 1
    page_obj = paginator.get_page(page_number)
    b=a.count()
    try:
        c=following.objects.filter(user=request.user).count()
    except :
        c=0
    try:    
        d=following.objects.filter(people=request.user).count()
    except Exception as e:
        print(e)
        d = 0
    print(c)
    print(d)
    return render(request, "network/mypage.html",{
            "following":c,
            "followers":d,
            'page_obj': page_obj
            
    })

##################################################################################################################################
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("network:index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")

##################################################################################################################################
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("network:index"))

##################################################################################################################################
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("network:index"))
    else:
        return render(request, "network/register.html")

##################################################################################################################################
@csrf_exempt
@login_required
def compose(request):
    #post must

    if request.method !="POST":
        return JsonResponse({"error":"POST request required"},status=400)
    # Get the json string
    data = json.loads(request.body)
    #get contents of email
    body = data.get("body", "")
    x=posts(body=body,
            sender=request.user

            )
    x.save()
    return JsonResponse({"message":"YEAAAAA"},status=201)

##################################################################################################################################
@login_required
def new(request):
    poss=posts.objects.all()
    poss = poss.order_by("-timestamp").all()
    paginator = Paginator(poss, 4) # Show 25 contacts per page.
    try:    
        page_number = request.GET.get('page')
    except Exception as e:
        print(e)
        page_number = 1
    page_obj = paginator.get_page(page_number)
    return JsonResponse([post.serialize() for post in page_obj], safe=False)#####have to continue to add likes here!

##################################################################################################################################
@login_required
def new2(request):
    poss=posts.objects.filter(sender=request.user)
    poss = poss.order_by("-timestamp").all()
    paginator = Paginator(poss, 4) # Show 25 contacts per page.
    try:    
        page_number = request.GET.get('page')
    except Exception as e:
        print(e)
        page_number = 1
    page_obj = paginator.get_page(page_number)
    return JsonResponse([post.serialize() for post in page_obj], safe=False)#####have to continue to add likes here!
##################################################################################################################################
@login_required
def new3(request):
    c=following.objects.filter(user=request.user).values_list('people', flat=True)
    poss=posts.objects.filter(sender__in=c)
    poss = poss.order_by("-timestamp").all()
    paginator = Paginator(poss, 4) # Show 25 contacts per page.
    try:    
        page_number = request.GET.get('page')
    except Exception as e:
        print(e)
        page_number = 1
    page_obj = paginator.get_page(page_number)
    return JsonResponse([post.serialize() for post in page_obj], safe=False)#####have to continue to add likes here!

##################################################################################################################################
@csrf_exempt
@login_required
def like(request, email_id):
    try:
        post = posts.objects.get(pk=email_id)
    except post.DoesNotExist:
        return JsonResponse({"error": "Post not found."}, status=404)
    if request.method !="POST":
        return JsonResponse({"error":"POST request required"},status=400)
        
    data = json.loads(request.body)
    user= request.user
    body = data.get("like", "")
    if Todo_likes.objects.filter(todo=post,user=request.user).exists():
        li = Todo_likes.objects.get(todo=post,user=request.user)
        li.delete()
    else:
        li=Todo_likes(todo=post,user=request.user)
        li.save()
    q1=Todo_likes.objects.filter(todo=post).count()
    post.likes=q1
    post.save()
    return JsonResponse({"message":"success","likes":q1},status=201)
    q1=Todo_likes.objects.filter(todo=post).count()
    post.likes=q1
    post.save()
    return JsonResponse({"message":"success","likes":q1},status=201)
##################################################################################################################################
@csrf_exempt
@login_required
def edit(request, email_id):
    try:
        post = posts.objects.get(pk=email_id)
    except post.DoesNotExist:
        return JsonResponse({"error": "Post not found."}, status=404)
    if request.method !="POST":
        return JsonResponse({"error":"POST request required"},status=400)
        
    data = json.loads(request.body)
    body = data.get("body", "")
    post.body=body
    post.save()
    return JsonResponse({"message":"success","body":post.body},status=201)

##################################################################################################################################

