from django.test import SimpleTestCase
from django.urls import reverse, resolve
from mainapp.views import signup, login, index, recipeDetails, migrate, recipe, add_recipe

class TestUrls(SimpleTestCase):

    def test_signup_url_resolves(self):
        url = reverse('signup')
        self.assertEquals(resolve(url).func, signup)

    def test_login_url_resolves(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, login)

    def test_index_url_resolves(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_recipeDetails_url_resolves(self):
        url = reverse('recipeDetails')
        self.assertEquals(resolve(url).func, recipeDetails)

    def test_migrate_url_resolves(self):
        url = reverse('migrate')
        self.assertEquals(resolve(url).func, migrate)

    def test_recipe_url_resolves(self):
        url = reverse('recipes')
        self.assertEquals(resolve(url).func, recipe)

    def test_add_recipe_url_resolves(self):
        url = reverse('add_recipe')
        self.assertEquals(resolve(url).func, add_recipe)
