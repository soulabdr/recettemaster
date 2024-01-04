from django.test import TestCase
from mainapp.models import Category, Recipe, Ingredient, Step

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(label='Test Category')

    def test_category_creation(self):
        self.assertEqual(self.category.label, 'Test Category')

class RecipeModelTest(TestCase):
    def setUp(self):
        self.recipe = Recipe.objects.create(
            title='Test Recipe',
            description='Test Description',
            duration='Test Duration',
            nbrPersons='Test Persons',
            nbrCalories='Test Calories',
            difficulty='Test Difficulty'
        )

    def test_recipe_creation(self):
        self.assertEqual(self.recipe.title, 'Test Recipe')

class IngredientModelTest(TestCase):
    def setUp(self):
        self.recipe = Recipe.objects.create(
            title='Test Recipe',
            description='Test Description',
            duration='Test Duration',
            nbrPersons='Test Persons',
            nbrCalories='Test Calories',
            difficulty='Test Difficulty'
        )
        self.ingredient = Ingredient.objects.create(
            description='Test Ingredient',
            recipe=self.recipe
        )

    def test_ingredient_creation(self):
        self.assertEqual(self.ingredient.description, 'Test Ingredient')

class StepModelTest(TestCase):
    def setUp(self):
        self.recipe = Recipe.objects.create(
            title='Test Recipe',
            description='Test Description',
            duration='Test Duration',
            nbrPersons='Test Persons',
            nbrCalories='Test Calories',
            difficulty='Test Difficulty'
        )
        self.step = Step.objects.create(
            description='Test Step',
            number=1,
            recipe=self.recipe
        )

    def test_step_creation(self):
        self.assertEqual(self.step.description, 'Test Step')
