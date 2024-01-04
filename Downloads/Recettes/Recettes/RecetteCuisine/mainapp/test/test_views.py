from django.test import TestCase, Client
from django.urls import reverse

class ViewsTestCase(TestCase):
    def test_signup(self):
        client = Client()


        response = client.post(reverse('signup'), {
            'email': 'test@example.com',
            'password1': 'password',
            'password2': 'password'
        })
        self.assertEqual(response.status_code, 302)
        response = client.post(reverse('signup'), {
            'email': 'test@example.com',
            'password1': 'password',
            'password2': 'password'
        })
        self.assertEqual(response.status_code, 200)
        response = client.post(reverse('signup'), {
            'email': 'test2@example.com',
            'password1': 'password1',
            'password2': 'password2'
        })
        self.assertEqual(response.status_code, 200)

    def test_index_view(self):
        client = Client()
        response = client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)


    def test_login_view(self):
        client = Client()
        response = client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_add_recipe_view(self):
        client = Client()
        response = client.get(reverse('add_recipe'))
        self.assertEqual(response.status_code, 200)  # Vérifiez que la page add_recipe renvoie un code 200
