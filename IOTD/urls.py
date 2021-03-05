from django.urls import path
from IOTD import views
app_name = 'IOTD'
urlpatterns = [
path('', views.home, name='home'),
path('upload/',views.upload,name='upload'),
path('vote-image/',views.voteImage,name='voteImage'),
path('login/',views.login,name='login'),
path('my-account/',views.myAccount,name='myAccount')
]
