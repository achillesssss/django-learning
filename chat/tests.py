from django.test import TestCase, Client, RequestFactory
from django.utils import timezone

from django.contrib.auth.models import User
from .models import Message

# authenticated information

USR = 'admin'
PWD = 'admin123456'
EMAIL = 'admin@admin.vn'

# unauthenticated information

UNUSR = 'account'
UNPWD = 'asdfasdf123    '
UNEMAIL = 'account@gmail.com'

# temporary data for Message

CONTENT = 'asdfasdf'
DATE = timezone.now()



class AuthenticationTestCase(TestCase):

    def setUp(self):
        #every tests need a client 
        self.client = Client()

        self.admin = User.objects.create_user(username=USR, password=PWD)
        self.admin.save()

    def test_signup_fail(self):
        response = self.client.get('/signup')
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/signup/', {
            'username': UNUSR,
            'password': UNPWD,
            'password_confirmation': UNPWD,
            })
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/signup/', {
            'username': UNUSR,
            'password1': UNPWD,
            'password2': UNPWD,
            })
        self.assertEqual(response.status_code, 302)        

    def test_redirect_when_not_login(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)

    def test_login_sucessfully(self):
        login = self.client.login(username=USR, password=PWD)
        self.assertTrue(login)
        
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_send_message(self):
        login = self.client.login(username=USR, password=PWD)
        self.assertTrue(login)

        response = self.client.post('/', {
            'content': CONTENT,
            })
        self.assertEqual(response.status_code, 200)

    