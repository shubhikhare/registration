from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import Http404, HttpResponse
from django.contrib.auth.models import User
from .models import R_User
from django.template import RequestContext

# Create your views here.
def home(request):
	return render_to_response("regis/index.html",context_instance=RequestContext(request))
def get(self, request):
	template_name = "display.html"
	return render(request, self.template_name)

def display(request, zeal):
	zeal_id = get_object_or_404(R_User, pk=zeal)
	template = get_template('display.html')
	variables = ({ 'name':name,
		'email':email,
		'course':course,
		'branch':branch,
		'contact':contact,
		'college':college,
		'year':year
		})
  	output = template.render(variables)
  	return HttpResponse(output)


