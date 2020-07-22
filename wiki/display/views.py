from django.shortcuts import render
from django.http import HttpResponse
from encyclopedia.util import get_entry
from django.http import Http404
from markdown2 import markdown

# Create your views here.

def index(request, entry): 
	response = get_entry(entry)
	print(entry)
	print('you are here!')
	if (response == None):
		return render(request, "display/error.html")
	else:
		response = markdown(response)
		return render(request, "display/index.html", {
			"title": entry,
			"response": response
			})
	# return render(request, response)
