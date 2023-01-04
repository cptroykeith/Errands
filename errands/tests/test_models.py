from django.test import TestCase
from authentication.models import User
from errands.models import errands

class TestModel(TestCase):
    def test_should_create_user(self):
        user=User.objects.create_user(username='username', email='email@app.com')
        user.set_password('password12!')
        user.save()

        Errands = errands(owner=user, title='buy milk',description='get it done')

        Errands.save()

        self.assertEqual(str(Errands), 'buy milk')

