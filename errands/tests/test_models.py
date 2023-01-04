
from authentication.models import User
from errands.models import errands
from utils.setup_test import TestSetup

class TestModel(TestSetup):
    def test_should_create_user(self):
        user=self.create_test_user()

        Errands = errands(owner=user, title='buy milk',description='get it done')
        Errands.save()

        self.assertEqual(str(Errands), 'buy milk')

