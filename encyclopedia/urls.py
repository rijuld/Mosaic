from django.urls import path


from . import views
app_name="wiki"

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.title, name="title"),
    path("a/add",views.add,name="add"),
    path("hrllo/hi",views.info, name="info"),
    path("edit/<str:title>",views.edit, name="edit"),
    path("a/random",views.random,name="random")
    


]

