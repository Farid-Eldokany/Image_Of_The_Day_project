from django import forms
from django.contrib.auth.models import User
from IOTD.models import UserProfile,Vote
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
        exclude=('user',)

        

