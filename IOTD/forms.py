from django import forms
from django.contrib.auth.models import User
from IOTD.models import UserProfile,Vote,Day,Total,Report
class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ('username', 'password',)
class UserProfileForm(forms.ModelForm):
    likes= forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    dislikes= forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    image_id=forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = UserProfile
        fields = ('picture','name')
class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        exclude=('vote_id','vote_type')
class DayForm(forms.ModelForm):
    class Meta:
        model=Day
        exclude=('day',)
class TotalForm(forms.ModelForm):
    class Meta:
        model=Total
        exclude=("likes","dislikes","user")
class ReportForm(forms.ModelForm):
    class Meta:
        model=Report
        exclude=("report_id","image_id","username",'reason',)
        

