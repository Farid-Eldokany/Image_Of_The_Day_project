from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.shortcuts import redirect
from IOTD.forms import UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
def home(request):

	context_dict = {}
	response = render(request, 'IOTD/homepage.html', context=context_dict)

	return response
	#return HttpResponse("This is the homepage.")

def voteImage(request):
	return HttpResponse("Vote image here.")
def user_login(request):
	#IOTD/loginpage.html
	
	user_form = UserForm(request.POST)
	if request.method == 'POST':
		if 'Login' in request.POST:
			
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = authenticate(username=username, password=password)
			if user:
				if user.is_active:
					login(request, user)
					return redirect(reverse('IOTD:home'))
				else:
					# An inactive account was used - no logging in!
					return HttpResponse("Your account is disabled.")
			else:
				# Bad login details were provided. So we can't log the user in.
				print(f"Invalid login details: {username}, {password}")
				return HttpResponse("Invalid login details supplied.")
		elif 'Signup' in request.POST:
			if user_form.is_valid():
				user = user_form.save()
				user.set_password(user.password)
				user.save()
				return redirect(reverse('IOTD:home'))
				
			else:
				print(user_form.errors)


	return render(request,'IOTD/loginpage.html',context = {'user_form': user_form})

def upload(request):
	return HttpResponse("Upload here.")
def myAccount(request):
	return HttpResponse("This is the my account page.")
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return redirect(reverse('IOTD:home'))