from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.shortcuts import redirect
from IOTD.forms import UserForm, UserProfileForm,VoteForm,ReportForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from IOTD.models import UserProfile,Vote,Day,Total,Report
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
import datetime
from django.core.paginator import Paginator
#first page that the user sees
def home(request):
    context_dict={}
    #gets the the todays day name
    now = datetime.datetime.now()
    today=now.strftime("%A")
    try:
        day=Day.objects.get()
        #checks if a new day began
        if(str(day.day)!=today):
            #removes all the votes and images related entries in the database
            Vote.objects.all().delete()
            UserProfile.objects.all().delete()
            #sets todays day name as the current day 
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
    #incase there is no day set, this code sets a day in the database
    except ObjectDoesNotExist:
        set_day = Day.objects.create(day=today)
        return render(request, 'IOTD/homepage.html')
#takes the votes of the user on the image to change its dislikes/likes and also lets the user report it        
@login_required
def voteImage(request):
    contact_list = UserProfile.objects.all()
    paginator = Paginator(contact_list, 10) # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    username=str(request.user.username)
    vote_instance = Vote()
    report_instance=Report()
    #checks if the request method type is post
    if request.method == 'POST':
        report_form=ReportForm(request.POST,instance=report_instance)
        vote_form = VoteForm(request.POST,instance=vote_instance)
        #checks if the voting is valid
        if vote_form.is_valid():
            vote = vote_form.save(commit=False)
            #checks if the user liked an image
            if 'like' in request.POST:
                image_id=request.POST['like']
                userprofile = UserProfile.objects.get(image_id=image_id)
                total=Total.objects.get(user=userprofile.user)
                try:
                    prev_vote=Vote.objects.get(vote_id=username+image_id)
                    prev_vote_type=prev_vote.vote_type
                    #checks if the user had disliked the image before liking it 
                    if(prev_vote_type=='dislike'):
                        #the like is removed from the image and a dislike is added
                        userprofile.dislikes-=1
                        userprofile.likes+=1
                        prev_vote.vote_type='like'
                        total.likes+=1
                        total.dislikes-=1
                        total.save()
                        userprofile.save()
                        prev_vote.save()
                    #checks if the user had liked the image before liking it    
                    elif(prev_vote_type=='like'):
                        #the like is removed from the image
                        userprofile.likes-=1
                        prev_vote.delete()
                        total.likes-=1
                        total.save()
                        userprofile.save()
                    return redirect(reverse('IOTD:voteImage'))
                #incase the user never voted the image before
                except Vote.DoesNotExist:
                    userprofile.likes+=1
                    total.likes+=1
                    total.save() 
                    vote_type='like'
            #checks if the user liked an image
            elif 'dislike' in request.POST:
                image_id=request.POST['dislike']
                userprofile = UserProfile.objects.get(image_id=image_id)
                total=Total.objects.get(user=userprofile.user)
                try:
                    prev_vote=Vote.objects.get(vote_id=username+image_id)
                    prev_vote_type=prev_vote.vote_type
                    #checks if the user had liked the image before disliking it 
                    if(prev_vote_type=='like'):
                        #the dislike is removed from the image and a like is added
                        userprofile.likes-=1
                        userprofile.dislikes+=1
                        prev_vote.vote_type='dislike'
                        total.likes-=1
                        total.dislikes+=1
                        total.save()
                        userprofile.save()
                        prev_vote.save()
                    #checks if the user had disliked the image before disliking it     
                    elif(prev_vote_type=='dislike'):
                        #the dislike is removed from the image
                        userprofile.dislikes-=1
                        total.dislikes-=1
                        total.save()
                        prev_vote.delete()
                        userprofile.save()
                    return redirect(reverse('IOTD:voteImage'))
                #incase the user never voted the image before
                except Vote.DoesNotExist:
                    userprofile.dislikes+=1
                    total.dislikes+=1
                    total.save()
                    vote_type='dislike'
            #checks if the user reported an image
            elif 'report' in request.POST:
                report_id=username+request.POST['report']
                if report_form.is_valid():
                    report = report_form.save(commit=False)
                    report.report_id=report_id
                    report.username=username
                    report.image_id=request.POST['report']
                    report.reason=''
                    report.save()
                    
                return redirect(reverse('IOTD:image_report', args=(report_id,)))
            else:
                return error(request,'Error occured refresh the website.')
            userprofile.save()
            vote.vote_id=username+image_id
            vote.vote_type=vote_type
            vote.save()
    else:
        vote_form = VoteForm()
    return render(request,"IOTD/vote-image.html",context={'contacts':contacts,'vote_form':vote_form})
# displays the form for the user login and registeration
def user_login(request):
    # IOTD/loginpage.html
    user_form = UserForm(request.POST)
    #checks if the request method type is post
    if request.method == 'POST':
        #checks if the user has pressed the login submit button
        if 'Login' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            #checks if the entered data is valid and matches a user data
            if user:
                #checks if the user account is still valid
                if user.is_active:
                    login(request, user)
                    return redirect(reverse('IOTD:home'))
                else:
                    # An inactive account was used - no logging in!
                    return error(request,"Your account is disabled.")
            else:
                # Bad login details were provided. So we can't log the user in.
                return error(request,"Invalid login details supplied.")
        #checks if the user has pressed the register submit button
        elif 'Signup' in request.POST:
            #checks if the form submitted is valid
            if user_form.is_valid():
                user = user_form.save()
                user.set_password(user.password)
                total= Total(user=user)
                total.dislikes=0
                total.likes=0
                total.save()
                user.save()
                return error(request,'Thank you for registering.')
            else:
                 return error(request,"This username already exists.")
        else:
            print(user_form.errors)
    return render(request, 'IOTD/loginpage.html', context={'user_form': user_form})
#uploads the picture that the user uploads
@login_required
def upload(request):
    try:
        UserProfile_instance = UserProfile.objects.get(user=request.user)    
        UserProfile_instance.delete()
    except UserProfile.DoesNotExist:
        UserProfile_instance = UserProfile(user=request.user)
    #checks if the request method type is post
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, instance=UserProfile_instance)
        #checks if the form submitted is valid
        if profile_form.is_valid() :
            imageName=request.POST.get('name')
            try: 
                UserProfile.objects.get(name=request.user)
                return error(request,"This image name is already used.")
            except ObjectDoesNotExist:
                profile = profile_form.save(commit=False)
                profile.user = request.user
                profile.image_id=str(profile.user.username)+imageName
                #checks if a picture has been uploaded
                if 'picture' in request.FILES:
                    profile.picture = request.FILES['picture']
                else:
                    return error(request,"You have not uploaded a picture.")
                profile.save()
                return error(request,"Image uploaded succesfully.")
        else:
            print(profile_form.errors)
    else:
        profile_form = UserProfileForm(instance=UserProfile_instance)
        
    return render(request,'IOTD/upload.html',context = {'profile_form': profile_form})
#shows the image of the user that he uploaded
@login_required
def myAccount(request):
    try:
        #get the total likes and dislikes that the user has so far and also shows the current image he has uploaded if he did
        context_dict = {'image':UserProfile.objects.get(user=request.user),
                        "total":Total.objects.get(user=request.user)}
        response = render(request, 'IOTD/my-account.html', context=context_dict)
        return response
    #incase he didnt upload an image
    except UserProfile.DoesNotExist:
        return error(request,"You have not uploaded an image yet.")
def error(request,error):
    return render(request, 'IOTD/error.html', context={'error':error})
#logs out the user
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return redirect(reverse('IOTD:home'))
#requests a reason input from the user for the admin to know why the image is reported
def image_report(request,report_id):
    if'submit' in request.POST:
        reason=request.POST["reason"]
        report=Report.objects.get(report_id=report_id)
        if(reason==""):
            report.delete()
            return error(request,"No reason was submitted, therefore the report has been removed.")
        report.reason=reason
        report.save()
        return error(request,"Report submitted and will be reviewed shortly.")
    return render(request, 'IOTD/image_report.html', context={})
#shows the searched image
def image_search(request,profile):
    return render(request, 'IOTD/image_search.html', context={"image":UserProfile.objects.get(name=profile)}) 
