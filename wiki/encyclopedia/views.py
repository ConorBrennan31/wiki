from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from . import util
from django.shortcuts import redirect


def index(request):
	if (request.method =="POST"):
		data = request.POST.copy()
		data = data.get('q').lower()

		entries = util.list_entries()
		filtered_entries = [entry for entry in entries if data in entry.lower()]

		if (util.get_entry(data) != None):
			return redirect("display:index", data)

		elif (len(filtered_entries) > 0):
			return render(request, "encyclopedia/searchResults.html", {
				"entries": filtered_entries
				})

		elif(len(filtered_entries) == 0):
			return HttpResponse("Your query matched 0 pages")


	else:
	    return render(request, "encyclopedia/index.html", {
	        "entries": util.list_entries()
	    })

