from django.db import models

# Create your models here.


"""class Category(models.Model):
    label = models.CharField(max_length=50)


class Recipe(models.Model):
    title = models.TextField()
    description = models.TextField(null=True)
    duration = models.CharField(max_length=50)
    nbrPersons = models.CharField(max_length=50, null=True)
    nbrCalories = models.CharField(max_length=50, null=True)
    difficulty = models.CharField(max_length=50, null=True)
    categories = models.ManyToManyField(Category)
    imageUrl = models.CharField(max_length=100, null=True)


class Ingredient(models.Model):
    description = models.TextField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)


class Step(models.Model):
    descreption = models.TextField()
    number = models.IntegerField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)



class Client(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    password = models.TextField()

    def __str__(self):
        return self.email


class Comment(models.Model):
    text = models.TextField()
    Client = models.ForeignKey(Client, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)


class Rating(models.Model):
    rate = models.IntegerField()
    Client = models.ForeignKey(Client, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
"""
from django.db import models

class Category(models.Model):
    label = models.CharField(max_length=50)

class Recipe(models.Model):
    title = models.TextField()
    description = models.TextField(null=True)
    duration = models.CharField(max_length=50)
    nbrPersons = models.CharField(max_length=50, null=True)
    nbrCalories = models.CharField(max_length=50, null=True)
    difficulty = models.CharField(max_length=50, null=True)
    categories = models.ManyToManyField(Category)
    imageUrl = models.ImageField(upload_to='recipe_images', null=True, blank=True)


class Ingredient(models.Model):
    description = models.TextField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

class Step(models.Model):
    description = models.TextField()  # Correction de la faute de frappe ici (descreption -> description)
    number = models.IntegerField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

class Client(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    password = models.TextField()

    def __str__(self):
        return self.email

class Comment(models.Model):
    text = models.TextField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)  # Correction de la casse (Client -> client)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

class Rating(models.Model):
    rate = models.IntegerField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)  # Correction de la casse (Client -> client)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
