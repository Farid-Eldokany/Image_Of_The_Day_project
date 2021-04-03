from django.test import TestCase,Client
from IOTD.models import *
from django.contrib.auth.models import User
from IOTD.views import *
# Create your tests here.
class UserProfileMethodTests(TestCase):
    def test_ensure_likes_and_dislikes_are_positive(self):
        """
        Tests creation of a user and a user profile.
        """
        self.picture="C:/Users/farid/Desktop/test.jpg"
        
        self.user=User.objects.create_user("test","test")
        self.userprofile=UserProfile.objects.create(user=self.user,picture=self.picture,likes=0,dislikes=0,name="test",image_id="testtest")
        self.userprofile.save()
        self.userprofile2=UserProfile.objects.get(user=self.user)
        self.assertEqual((self.userprofile2.likes == 0 and self.userprofile2.dislikes==0 and self.userprofile2.user==self.user), True)
        self.assertEqual((self.userprofile2.name=="test" and self.userprofile2.image_id=="testtest"), True)
        self.assertEqual((self.userprofile2.picture=="C:/Users/farid/Desktop/test.jpg" ), True)
    def test_all_views_for_not_logged_in_users(self):
        """
        Checks if pages and restricted images are displayed correctly for a user that is not logged in
        """
        response = self.client.get(reverse('IOTD:home'))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('IOTD:login'))
        self.assertEqual(response.status_code, 200)
        #user gets redirected to login for these restricted pages that require logging in
        response = self.client.get(reverse('IOTD:voteImage'))
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('IOTD:upload'))
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('IOTD:myAccount'))
        self.assertEqual(response.status_code, 302)
    def test_all_views_for_logged_in_users(self):
        # send login data
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        self.usertest=User.objects.create_user(**self.credentials)
        c = Client()
        self.credentials.update({'Login':'Login'})
        response = c.post(reverse('IOTD:login'), self.credentials, follow=True)
        # should be logged in now
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['user'].is_authenticated, True)
        self.assertEqual(response.status_code, 200)
        #when user is logged in he is able to acess the restricted pages that he wasnt able to acess when he
        #wasnt logged in
        response = c.get(reverse('IOTD:voteImage'))
        self.assertEqual(response.status_code, 200)
        response = c.get(reverse('IOTD:upload'))
        self.assertEqual(response.status_code, 200)
        response = c.get(reverse('IOTD:myAccount'))
        self.assertEqual(response.status_code, 200)
        response = c.get(reverse('IOTD:logout'))
        self.assertEqual(response.status_code, 302)
        response = c.get(reverse('IOTD:upload'))
        self.assertEqual(response.status_code, 302)
    def test_upload_view_for_logged_in_users_and_vote_and_report(self):
        credentials = {
            'username': 'testuser',
            'password': 'secret'}
        user=User.objects.create_user(**credentials)
        c = Client()
        credentials = {
            'username': 'testuser',
            'password': 'secret',
            'Login':'Login'}
        response = c.post(reverse('IOTD:login'), credentials, follow=True) 
        self.assertEqual(response.context['user'].is_authenticated, True)
        #uploading
        with open('C:/Users/farid/Desktop/test.jpg','rb') as fp:
            response = c.post(reverse('IOTD:upload'), {'name': 'test', 'picture': fp},follow=True) 
            self.assertEqual(response.status_code, 200)
        #############
        userprofile=UserProfile.objects.create(user=user,picture='C:/Users/farid/Desktop/test.jpg',likes=0,dislikes=0,name="test",image_id="testtest")
        userprofile.save()
        self.assertEqual(userprofile.likes, 0)
        total=Total.objects.create(user=user,likes=0,dislikes=0)
        response=c.post(reverse('IOTD:voteImage'), {'like':"testtest"}) 
        self.assertEqual(response.status_code, 200)
        userprofile2=UserProfile.objects.get(user=user)
        #simulating user liking image once
        self.assertEqual(userprofile2.likes, 1)
        ###########
        c.post(reverse('IOTD:voteImage'), {'like':"testtest"})
        userprofile2=UserProfile.objects.get(user=user)
        #simulating user liking image twice
        self.assertEqual(userprofile2.likes, 0)
        ###########
        c.post(reverse('IOTD:voteImage'), {'like':"testtest"})
        userprofile2=UserProfile.objects.get(user=user)
        #simulating user liking image then disliking
        self.assertEqual(userprofile2.likes, 1)
        self.assertEqual(userprofile2.dislikes, 0)
        c.post(reverse('IOTD:voteImage'), {'dislike':"testtest"})
        userprofile2=UserProfile.objects.get(user=user)
        self.assertEqual(userprofile2.likes, 0)
        self.assertEqual(userprofile2.dislikes, 1)
        #############
        userprofile2=UserProfile.objects.get(user=user)
        #simulating user liking image after disliking it
        self.assertEqual(userprofile2.likes, 0)
        self.assertEqual(userprofile2.dislikes, 1)
        c.post(reverse('IOTD:voteImage'), {'like':"testtest"})
        userprofile2=UserProfile.objects.get(user=user)
        self.assertEqual(userprofile2.likes, 1)
        self.assertEqual(userprofile2.dislikes, 0)
        #############
        c.post(reverse('IOTD:voteImage'), {'like':"testtest"})
        userprofile2=UserProfile.objects.get(user=user)
        self.assertEqual(userprofile2.dislikes, 0)
        #simulating user disliking image once
        c.post(reverse('IOTD:voteImage'), {'dislike':"testtest"})
        userprofile2=UserProfile.objects.get(user=user)
        self.assertEqual(userprofile2.dislikes, 1)
        ###########
        #simulating user disliking image twice
        self.assertEqual(userprofile2.dislikes, 1)
        c.post(reverse('IOTD:voteImage'), {'dislike':"testtest"})
        userprofile2=UserProfile.objects.get(user=user)
        self.assertEqual(userprofile2.dislikes, 0)
        ###########
        #simulating user reporting an image
        response=c.post(reverse('IOTD:voteImage'), {'report':"testtest"},follow=True)
        #user redirected to report page to submit the reason for the report
        self.assertEqual(response.status_code, 200)
        #submits report reason
        report_id=user.username+userprofile2.image_id
        reason="dupe"
        c.post(response.request['PATH_INFO'],{'submit':"submit","reason":reason})
        #checks if the reason is actually submitted
        report=Report.objects.get(report_id=report_id)
        self.assertEqual(report.reason, reason)
        