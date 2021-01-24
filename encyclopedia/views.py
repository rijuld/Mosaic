from django.shortcuts import render
from django.http import HttpResponse
from . import util
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
import markdown2
import random as rand
from datetime import datetime
from django.views import generic
from django.utils.safestring import mark_safe
from .models import Event
from .utils import Calendar
from datetime import *
import calendar 
from django.shortcuts import get_object_or_404
from .forms import EventForm
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from django.db.models import Count
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from auctions.models import User

class NewTaskForm(forms.Form):
	title = forms.CharField(label="Title")
	content=forms.CharField(widget=forms.Textarea)
class search(forms.Form):
	title =forms.CharField(label="search")
class k(forms.Form):
	b=forms.CharField(widget=forms.Textarea)




	# Add a new task:
def add(request):

	# Check if method is POST
	if request.method == "POST":

		# Take in the data the user submitted and save it as form
		form = NewTaskForm(request.POST)

		# Check if form data is valid (server-side)
		if form.is_valid():

			# Isolate the task from the 'cleaned' version of form data
			title = form.cleaned_data["title"]
			content= form.cleaned_data["content"]
			if util.get_entry(title)!=None:
				return HttpResponse("Ugh!,This entry already exists!")
			else:
				# Add the new task to our list of tasks
				util.save_entry(title, content)

				# Redirect user to list of tasks
				return HttpResponseRedirect(reverse("wiki:title",kwargs={'title':title}))


			

		else:

			# If the form is invalid, re-render the page with existing information.
			return render(request, "encyclopedia/add.html", {
				"form": form
			})

	return render(request, "encyclopedia/add.html", {
		"form": NewTaskForm()
	})



def index(request):

	fieldname = "title"
	most_common = Event.objects.values(fieldname).annotate(count=Count(fieldname)).order_by("-count")
	most_common=most_common.first()["title"]

	return render(request, "encyclopedia/index.html", {
		"entries": util.list_entries(),
		"mc":most_common
	})


def title(request, title):
	
	 
	global mdValue
	mdValue=util.get_entry(title)
	htmlValue=title
	if mdValue==None:
		return HttpResponse("<h1>Oops!, the requested page was not found, looks like someone forgot to add this page!</h1>")
	else:
		return render(request, "encyclopedia/page.html",{
		"title": htmlValue,
		"content":markdown2.markdown(util.get_entry(title))

	})
def info(request):
	if request.method=="POST":

		s=(request.POST['q'])
		mdValue=util.get_entry(s)
		if mdValue==None:
			test_list=util.list_entries()
			subs=s
			res = [s for s in test_list if subs.lower() in s.lower()]
			return render(request, "encyclopedia/sublist.html", {
			"res":res
		})

			
		else:

			return HttpResponseRedirect(reverse("wiki:title", kwargs={'title':s}))


	# Add a new task:
def edit(request,title):


	# Check if method is POST
	if request.method == "POST":
   
		content=(request.POST['content'])
		util.save_entry(title, content)
		return HttpResponseRedirect(reverse("wiki:title",kwargs={'title':title}))


	value=util.get_entry(title)
	#data_dict = {'b': value}
	#form = k(initial=data_dict)

	return render(request, "encyclopedia/edit.html", {
		"form": k(),
		"title":title,
		"content":value
		
})
def random(request):
	title=rand.choice(util.list_entries())
	return HttpResponseRedirect(reverse("wiki:title", kwargs={'title':title}))
	

class CalendarView(generic.ListView):
	model = Event
	template_name = 'encyclopedia/calendar.html'
	def get_queryset(self):
		return Event.objects.filter(user=self.request.user)
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		# use today's date for the calendar
		d = get_date(self.request.GET.get('day', None))
		d = get_date(self.request.GET.get('month', None))
		context['prev_month'] = prev_month(d)
		context['next_month'] = next_month(d)
		# Instantiate our calendar class with today's year and date
		cal = Calendar(d.year, d.month)

		# Call the formatmonth method, which returns our calendar as a table
		html_cal = cal.formatmonth(self.get_queryset(),withyear=True)
		context['calendar'] = mark_safe(html_cal)
		
		
		return context

def get_date(req_day):
	if req_day:
		year, month = (int(x) for x in req_day.split('-'))
		return date(year, month, day=1)
	return datetime.today()

def prev_month(d):
	first = d.replace(day=1)
	prev_month = first - timedelta(days=1)
	month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
	return month

def next_month(d):
	days_in_month = calendar.monthrange(d.year, d.month)[1]
	last = d.replace(day=days_in_month)
	next_month = last + timedelta(days=1)
	month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
	return month
	


#cal

	
def event(request, event_id=None):
	instance = Event()
	if event_id:
		instance = get_object_or_404(Event, pk=event_id)
	else:
		instance = Event()
	
	form = EventForm(request.POST or None, instance=instance)
	if request.POST and form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse('wiki:calendar'))
	return render(request, 'encyclopedia/event.html', {'form': form})


def event_add(request,title):
	instance = Event()
	form = EventForm(request.POST or None, instance=instance,initial={'title':title,'description':'blah blah blahhhhh!','user':request.user})
	if request.POST and form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse('wiki:calendar'))
	return render(request, 'encyclopedia/event.html', {'form': form})

	
class LineChartJSONView(BaseLineChartView):
	fieldname = "title"
	most_common = Event.objects.values(fieldname).annotate(count=Count(fieldname)).order_by("-count")[:5]
	datat = []
	datac= []
	for item in most_common: 
		datat.append(item["title"])
		datac.append(item["count"])

	def get_labels(self):
		fieldname = "title"
		most_common = Event.objects.values(fieldname).annotate(count=Count(fieldname)).order_by("-count")[:5]
		datat = []
		datac= []
		for item in most_common: 
			datat.append(item["title"])
			datac.append(item["count"])

		"""Return 7 labels for the x-axis."""
		return datat

	def get_providers(self):
		"""Return names of datasets."""
		return ["movies"]

	def get_data(self):
		"""Return 3 datasets to plot."""
		fieldname = "title"
		most_common = Event.objects.values(fieldname).annotate(count=Count(fieldname)).order_by("-count")[:5]
		datat = []
		datac= []
		for item in most_common: 
			datat.append(item["title"])
			datac.append(item["count"])


		return [datac]


line_chart = TemplateView.as_view(template_name='encyclopedia/line_chart.html')
line_chart_json = LineChartJSONView.as_view()