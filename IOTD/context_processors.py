from IOTD.models import UserProfile

def profiles(request):
    return {'profiles': UserProfile.objects.all()}