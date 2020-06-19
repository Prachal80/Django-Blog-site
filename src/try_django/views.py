from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template



def home_page(request):
	my_title = "Hello there....."
	return render(request,"home.html",{"title":my_title})

def about_page(request):
	return render(request,"about.html",{"title":"About"})

def contact_page(request):
	return render(request,"contact.html",{"title":"Contact"})	

def example_page(request):
	context = {"title": "Example"}
	template_name = "helloworld.html"
	template_obj = get_template(template_name)
	rendered_string = template_obj.render(context)
	# return HttpResponse(rendered_string)
	return render(request, "helloworld.html", {"title":"Example 1"})

