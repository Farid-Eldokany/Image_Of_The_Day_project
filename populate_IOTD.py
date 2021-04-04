import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Image_Of_The_Day_project.settings')
import django
django.setup()
from django.contrib.auth.models import User
from IOTD.models import UserProfile,Vote,Day,Total,Report
def populate():
    profiles=[{"model": "IOTD.userprofile", "pk": 34, "fields":
    {"user": 1, "picture": "profile_images/meme.jfif", "likes": 0, "dislikes": 0, "name": "Sleep Meme", "image_id": "user1Sleep Meme"}},
    {"model": "IOTD.userprofile", "pk": 36, "fields":
    {"user": 2, "picture": "profile_images/natural_photo.webp", "likes": 0, "dislikes": 0, "name": "Pretty Scenery", "image_id": "user2Pretty Scenery"}},
    {"model": "IOTD.userprofile", "pk": 37, "fields":
        {"user": 3, "picture": "profile_images/sphinx.jpg", "likes": 0, "dislikes": 0, "name": "Sphinx", "image_id": "user3Sphinx"}},
    {"model": "IOTD.userprofile", "pk": 38, "fields":
        {"user": 4, "picture": "profile_images/mona_lisa.jpg", "likes": 0, "dislikes": 0, "name": "Mona Lisa", "image_id": "user4Mona Lisa"}},
    {"model": "IOTD.userprofile", "pk": 39, "fields":
        {"user": 5, "picture": "profile_images/ghandi.jfif", "likes": 0, "dislikes": 0, "name": "Ghandi", "image_id": "user5Ghandi"}}]
    for profile in profiles:
        userprofile=profile["fields"]
        add_userProfile(userprofile["user"],userprofile["picture"],userprofile["likes"],userprofile["dislikes"],userprofile["name"],userprofile["image_id"])
def add_userProfile(user_id,picture,likes,dislikes,name,image_id):
    credentials = {
            'username': 'user'+str(user_id),
            'password': 'user'+str(user_id)}
    user=User.objects.create_user(**credentials)
    total= Total(user=user)
    total.dislikes=0
    total.likes=0
    total.save()
    p = UserProfile.objects.get_or_create(user=user,picture=picture,likes=likes,dislikes=dislikes,name=name,image_id=image_id)[0]
    p.save()
if __name__ == '__main__':
    print('Starting IOTD population script...')
    populate()