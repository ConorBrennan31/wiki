from django.shortcuts import render
from django.http import HttpResponse
from encyclopedia import util 
from django.shortcuts import redirect
from markdown2 import markdown
import random


# Create your views here.

def index(request):
	if (request.method == "POST"):
		data = request.POST.copy()
		title = data.get('title')
		contents = data.get('contents')
		if (util.get_entry(title) != None):
			raise Exception('An entry already exists with this title!')
		util.save_entry(title, contents)
		return redirect("display:index", title)
	return render(request, 'pages/index.html')

def editPage(request, title):
	contents = util.get_entry(title)

	if (request.method == "POST"):
		data = request.POST.copy()
		contents = data.get('contents')
		util.save_entry(title, contents)
		return redirect("display:index", title)
	else: 
		return render(request, 'pages/edit.html', {
			"title": title,
			"contents": contents
			})

def randomChoice(request):
	entries = util.list_entries()
	return redirect("display:index", random.choice(entries))
	return HttpResponse("Random page here")