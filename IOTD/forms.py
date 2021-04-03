from django import forms
from django.contrib.auth.models import User
from IOTD.models import UserProfile,Vote,Day,Total,Report
#form for logging in and registering in 
class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ('username', 'password',)
#form for uploading pictures
class UserProfileForm(forms.ModelForm):
    likes= forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    dislikes= forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    image_id=forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = UserProfile
        fields = ('picture','name')
#form for voting pictures
class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        exclude=('vote_id','vote_type')
#form for the day that shows the images
class DayForm(forms.ModelForm):
    class Meta:
        model=Day
        exclude=('day',)
#form for showing the total dislikes and likes that the user has
class TotalForm(forms.ModelForm):
    class Meta:
        model=Total
        exclude=("likes","dislikes","user")
#form for the reporting images
class ReportForm(forms.ModelForm):
    class Meta:
        model=Report
        exclude=("report_id","image_id","username",'reason',)
        

