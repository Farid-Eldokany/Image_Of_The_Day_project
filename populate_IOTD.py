import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Image_Of_The_Day_project.settings')
import django
django.setup()
from IOTD.models import UserProfile,Vote,Day,Total,Report
def populate():
    profiles=[{"model": "IOTD.userprofile", "pk": 34, "fields": 
    {"user": 16, "picture": "profile_images/meme_64TCkLD.jfif", "likes": 0, "dislikes": 0, "name": "Sleep Meme", "image_id": "user1Sleep Meme"}}, 
    {"model": "IOTD.userprofile", "pk": 36, "fields": 
    {"user": 17, "picture": "profile_images/natural_photo_KLNmkHB.webp", "likes": 0, "dislikes": 0, "name": "Pretty Scenery", "image_id": "user2Pretty Scenery"}}, 
    {"model": "IOTD.userprofile", "pk": 37, "fields": 
        {"user": 18, "picture": "profile_images/sphinx_QdqQ4Ha.jpg", "likes": 0, "dislikes": 0, "name": "Sphinx", "image_id": "user3Sphinx"}}, 
    {"model": "IOTD.userprofile", "pk": 38, "fields": 
        {"user": 19, "picture": "profile_images/mona_lisa_r564ppP.jpg", "likes": 0, "dislikes": 0, "name": "Mona Lisa", "image_id": "user4Mona Lisa"}}, 
    {"model": "IOTD.userprofile", "pk": 39, "fields": 
        {"user": 20, "picture": "profile_images/ghandi_UOC9ChI.jfif", "likes": 0, "dislikes": 0, "name": "Ghandi", "image_id": "user5Ghandi"}}]
    for profile in profiles:
        userprofile=profile["fields"]
        add_userProfile(userprofile["user"],userprofile["picture"],userprofile["likes"],userprofile["dislikes"],userprofile["name"],userprofile["image_id"])
def add_userProfile(user,picture,likes,dislikes,name,image_id):
    p = UserProfile.objects.get_or_create(user=user,picture=picture,likes=likes,dislikes=dislikes,name=name,image_id=image_id)[0]
    p.save()
if __name__ == '__main__':
    print('Starting IOTD population script...')
    populate()