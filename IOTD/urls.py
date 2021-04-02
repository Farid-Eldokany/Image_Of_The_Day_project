from django.urls import path
from IOTD import views
app_name = 'IOTD'
urlpatterns = [
path('', views.home, name='home'),
path('upload/',views.upload,name='upload'),

path('vote-image/',views.voteImage,name='voteImage'),

path('login/',views.user_login,name='login'),
path('my-account/',views.myAccount,name='myAccount'),

path('logout/', views.user_logout, name='logout'),
path('error/', views.error, name='error'),

path('<profile>/image_search/',views.image_search,name="image_search"),
path('home/<report_id>/report/',views.image_report,name="image_report"),
]