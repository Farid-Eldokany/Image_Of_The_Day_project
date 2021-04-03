from IOTD.models import UserProfile
from django.utils.datastructures import MultiValueDictKeyError
from django.core.exceptions import ObjectDoesNotExist
# loads the base.html with the user profiles
def profiles(request):
    data={}
    data['profiles']=UserProfile.objects.all()
    data['profile']="empty"
    try:
        search=request.POST["search"]
        profile=UserProfile.objects.get(name=search)
        data['profile']=profile
        return data
    except MultiValueDictKeyError:    
        return data
    except ObjectDoesNotExist:
        return data




       