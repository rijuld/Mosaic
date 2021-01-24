
from django.urls import path

from . import views
app_name="network"
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("follow", views.follow, name="follow"),
    path("compos",views.compose,name="compose"),
    path("new",views.new,name="new"),
    path("new2",views.new2,name="new2"),
    path("new3",views.new3,name="new3"),
    path("like/<int:email_id>",views.like,name="like"),
    path("edit/<int:email_id>",views.edit,name="edit"),#this is more like the toggling button
    path("mypage", views.mypage, name="mypage"),
    
]
