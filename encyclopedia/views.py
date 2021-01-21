from django.shortcuts import render
from django.http import HttpResponse
from . import util
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
import markdown2
import random as rand

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
	return render(request, "encyclopedia/index.html", {
		"entries": util.list_entries()
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
	

	


	




	




			






