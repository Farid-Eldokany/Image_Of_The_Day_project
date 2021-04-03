from django.db import models
from django.template.defaultfilters import slugify
from django.db import models
from django.contrib.auth.models import User
#model for uploading pictures
class UserProfile(models.Model):
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
#model for voting pictures
class Vote(models.Model):
    vote_id=models.CharField(max_length=128,primary_key=True,unique=True)
    vote_type=models.CharField(max_length=128,default='')
#model for the day that shows the images
class Day(models.Model):
    day=models.CharField(max_length=128)
#model for showing the total dislikes and likes that the user has
class Total(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
#model for the reporting images
class Report(models.Model):
    report_id=models.CharField(max_length=128,primary_key=True,unique=True)
    image_id=models.CharField(max_length=128,default='')
    username=models.CharField(max_length=128,default='')
    reason=models.CharField(max_length=128,default='')
    def __str__(self):
        return f"{self.image_id}"
