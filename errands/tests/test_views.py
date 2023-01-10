from utils.setup_test import TestSetup
from authentication.models import User
from errands.models import errands
from django.urls import reverse


class TestModel(TestSetup):

    def test_should_create_aerrand(self):

        user = self.create_test_user()
        self.client.post(reverse("login"), {
            'username': user.username,
            'password': 'password12!'
        })

        Errands = errands.objects.all()

        self.assertEqual(Errands.count(), 0)

        response = self.client.post(reverse('create-errands'), {
            'owner': user,
            'title': "Hello do this",
            'description': "Remember to do this"
        })

        updated_Errands = errands.objects.all()

        self.assertEqual(updated_Errands.count(), 1)

        self.assertEqual(response.status_code, 302)