"""RecetteCuisine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mainapp import views

"""urlpatterns = [
    path('', views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path('index/', views.index, name='index'),
    path('recipeDetails/', views.recipeDetails, name='recipeDetails'),
    path("migrate/", views.migrate, name="migrate"),
    path("recipes/", views.recipe, name="recipes"),
]"""


urlpatterns = [
    path('', views.signup, name='signup'),  # Redirection vers la vue d'inscription comme page d'accueil
    path('login/', views.login, name='login'),  # URL pour la connexion
    path('index/', views.index, name='index'),  # URL pour la page après la connexion
    path('recipeDetails/', views.recipeDetails, name='recipeDetails'),
    path('migrate/', views.migrate, name='migrate'),
    path('recipes/', views.recipe, name='recipes'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    # Autres URLs de votre application...
]

