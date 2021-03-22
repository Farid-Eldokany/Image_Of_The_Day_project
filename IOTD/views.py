from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.shortcuts import redirect
from IOTD.forms import UserForm, UserProfileForm,VoteForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from IOTD.models import UserProfile,Vote

def home(request):
	context_dict = {'images':UserProfile.objects.all().order_by('-likes')}
	response = render(request, 'IOTD/homepage.html', context=context_dict)
	return response
@login_required
def voteImage(request):
    print(request.POST)
    try:
        vote_instance = Vote.objects.get(user=request.user)
    except Vote.DoesNotExist:
        vote_instance = Vote(user=request.user)
    if request.method == 'POST':
        vote_form = VoteForm(request.POST,instance=vote_instance)
        if vote_form.is_valid():
            vote = vote_form.save(commit=False)
            
            if 'like' in request.POST:
                userprofile = UserProfile.objects.get(image_id=request.POST['like'])
                userprofile.likes+=1
                
            elif 'dislike' in request.POST:
                userprofile = UserProfile.objects.get(image_id=request.POST['dislike'])
                userprofile.dislikes+=1
            userprofile.save()
            vote.user = request.user
            vote.save()
    else:
        vote_form = VoteForm(instance=vote_instance)

    return render(request,"IOTD/vote-image.html",context={'images':UserProfile.objects.all(),'vote_form':vote_form})
def user_login(request):
	# IOTD/loginpage.html
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
	return render(request, 'IOTD/loginpage.html', context={'user_form': user_form})
@login_required
def upload(request):
    try:
        UserProfile_instance = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        UserProfile_instance = UserProfile(user=request.user)
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, instance=UserProfile_instance)
        if profile_form.is_valid() :
            imageName=request.POST.get('name')
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.image_id=str(profile.user.username)+imageName
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
        else:
            print(profile_form.errors)
    else:
        profile_form = UserProfileForm(instance=UserProfile_instance)
        
    return render(request,'IOTD/upload.html',context = {'profile_form': profile_form})
@login_required
def myAccount(request):
    context_dict = {'image':UserProfile.objects.get(user=request.user)}
    response = render(request, 'IOTD/my-account.html', context=context_dict)
    return response
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return redirect(reverse('IOTD:home'))
