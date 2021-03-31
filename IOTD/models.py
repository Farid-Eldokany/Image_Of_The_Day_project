from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
	# This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    name=models.CharField(max_length=128,default='')
    image_id=models.CharField(max_length=128)
    def __str__(self):
        return f"{self.name}"
    class Meta:
        ordering = ['-likes']
class Vote(models.Model):
    vote_id=models.CharField(max_length=128,primary_key=True,unique=True)
    vote_type=models.CharField(max_length=128,default='')
class Day(models.Model):
    day=models.CharField(max_length=128)
class Total(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
class Report(models.Model):
    report_id=models.CharField(max_length=128,primary_key=True,unique=True)
    image_id=models.CharField(max_length=128,default='')
    username=models.CharField(max_length=128,default='')
    reason=models.CharField(max_length=128,default='')
    def __str__(self):
        return f"{self.image_id}"
