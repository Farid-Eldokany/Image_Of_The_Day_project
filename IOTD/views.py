from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.shortcuts import redirect
from IOTD.forms import UserForm, UserProfileForm,VoteForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from IOTD.models import UserProfile,Vote,Day,Total
from django.core.exceptions import ObjectDoesNotExist
import datetime
def home(request):
    context_dict={}
    now = datetime.datetime.now()
    today=now.strftime("%A")
    try:
        day=Day.objects.get()
        if(str(day.day)!=today):
            Vote.objects.all().delete()
            UserProfile.objects.all().delete()
            day.day=today
            day.save()
            return render(request, 'IOTD/homepage.html')
        else:
            context_dict = {'images':UserProfile.objects.all().order_by('-likes')}
            try:
                response = render(request, 'IOTD/homepage.html', context=context_dict)
                return response
            except ValueError:
                return render(request, 'IOTD/homepage.html')
    except ObjectDoesNotExist:
        set_day = Day.objects.create(day=today)
        return render(request, 'IOTD/homepage.html')
        
@login_required
def voteImage(request):
    username=str(request.user.username)
    vote_instance = Vote()
    if request.method == 'POST':
        vote_form = VoteForm(request.POST,instance=vote_instance)
        if vote_form.is_valid():
            vote = vote_form.save(commit=False)
            if 'like' in request.POST:
                image_id=request.POST['like']
                userprofile = UserProfile.objects.get(image_id=image_id)
                total=Total.objects.get(user=userprofile.user)
                try:
                    prev_vote=Vote.objects.get(vote_id=username+image_id)
                    prev_vote_type=prev_vote.vote_type
                    if(prev_vote_type=='dislike'):
                        userprofile.dislikes-=1
                        userprofile.likes+=1
                        prev_vote.vote_type='like'
                        total.likes+=1
                        total.dislikes-=1
                        total.save()
                        userprofile.save()
                        prev_vote.save()
                        
                    elif(prev_vote_type=='like'):
                        userprofile.likes-=1
                        prev_vote.delete()
                        total.likes-=1
                        total.save()
                        userprofile.save()
                    return redirect(reverse('IOTD:voteImage'))
                except Vote.DoesNotExist:
                    userprofile.likes+=1
                    total.likes+=1
                    total.save() 
                    vote_type='like'
            elif 'dislike' in request.POST:
                image_id=request.POST['dislike']
                userprofile = UserProfile.objects.get(image_id=image_id)
                total=Total.objects.get(user=userprofile.user)
                try:
                    prev_vote=Vote.objects.get(vote_id=username+image_id)
                    prev_vote_type=prev_vote.vote_type
                    if(prev_vote_type=='like'):
                        userprofile.likes-=1
                        userprofile.dislikes+=1
                        prev_vote.vote_type='dislike'
                        total.likes-=1
                        total.dislikes+=1
                        total.save()
                        userprofile.save()
                        prev_vote.save()
                        
                    elif(prev_vote_type=='dislike'):
                        userprofile.dislikes-=1
                        total.dislikes-=1
                        total.save()
                        prev_vote.delete()
                        userprofile.save()
                    return redirect(reverse('IOTD:voteImage'))
                except Vote.DoesNotExist:
                    userprofile.dislikes+=1
                    total.dislikes+=1
                    total.save()
                    vote_type='dislike'
            userprofile.save()
            vote.vote_id=username+image_id
            vote.vote_type=vote_type
            vote.save()
    else:
        vote_form = VoteForm()
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
                    return error(request,"Your account is disabled.")
            else:
                # Bad login details were provided. So we can't log the user in.
                print(f"Invalid login details: {username}, {password}")
                return error(request,"Invalid login details supplied.")
        elif 'Signup' in request.POST:
            if user_form.is_valid():
                user = user_form.save()
                user.set_password(user.password)
                total= Total(user=user)
                total.dislikes=0
                total.likes=0
                total.save()
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
            else:
                return error(request,"You have not uploaded a picture.")
            profile.save()
        else:
            print(profile_form.errors)
    else:
        profile_form = UserProfileForm(instance=UserProfile_instance)
        
    return render(request,'IOTD/upload.html',context = {'profile_form': profile_form})
@login_required
def myAccount(request):
    try:
        context_dict = {'image':UserProfile.objects.get(user=request.user),
                        "total":Total.objects.get(user=request.user)}
        response = render(request, 'IOTD/my-account.html', context=context_dict)
        return response
    except UserProfile.DoesNotExist:
        return error(request,"You have not uploaded an image yet.")
def error(request,error):
    return render(request, 'IOTD/error.html', context={'error':error})
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return redirect(reverse('IOTD:home'))
