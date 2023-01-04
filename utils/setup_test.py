from django.test import TestCase
from authentication.models import User

class TestSetup(TestCase):

    def setUp(self):
        print("Test started")
        self.user={
            "username": "username",
            "email": "email@gmail.com",
            "password": "password",
             "password2": "password"
            }
    def create_test_user(self):
        user=User.objects.create_user(username='username', email='email@app.com')
        user.set_password('password12!')
        user.save()
        return user

    def create_test_user_two(self):
        user=User.objects.create_user(username='username2', email='email2@app.com')
        user.set_password('password12!')
        user.save()
        return user


    def tearDown(self):
        print('Test finished')
        return super().tearDown()