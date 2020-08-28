from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("listing/<str:title>",views.listing,name="listing"),
    path("watch",views.watch,name="watchlist"),
    path('createlisting',views.createlisting,name="createlisting"),
    path("category",views.category,name="category"),
    path("add/<str:title>",views.add,name="add"),
    path("remove/<str:title>",views.remove,name="remove"),
    path("subcategory/<str:title>",views.subcategory,name="subcategory"),
    path('mylist',views.mylist,name="mylist"),
    path('close/<str:title>',views.close,name="close"),
    path("won", views.won, name="won")
    
    
]
