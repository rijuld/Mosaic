from django.urls import path
from django.conf.urls import url
from .views import line_chart, line_chart_json

from . import views
app_name="wiki"

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.title, name="title"),
    path("a/add",views.add,name="add"),
    path("hrllo/hi",views.info, name="info"),
    path("edit/<str:title>",views.edit, name="edit"),
    path("a/random",views.random,name="random"),
    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'), 
    url(r'^event/new/$', views.event, name='event_new'),
    url(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
    path("event/<str:title>", views.event_add, name="event_add"),
    path('chart/', line_chart, name='line_chart'),
    path('chartJSON/', line_chart_json, name='line_chart_json'),


    # here


]

