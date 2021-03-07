from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):

	context_dict = {}
	response = render(request, 'IOTD/homepage.html', context=context_dict)

	return response
	#return HttpResponse("This is the homepage.")
def voteImage(request):
	return HttpResponse("Vote image here.")
def login(request):
	return HttpResponse("Login here.")
def upload(request):
	return HttpResponse("Upload here.")
def myAccount(request):
	return HttpResponse("This is the my account page.")