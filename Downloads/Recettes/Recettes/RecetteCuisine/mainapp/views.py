from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import auth
from .models import Client
from .models import *
from .migrationscript import fill_database

# Create your views here.
def index(request):
     template = get_template('index.html')
     return HttpResponse(template.render())
def recipeDetails(request):
     tempate = get_template('recipeDetails.html')
     return HttpResponse(tempate.render())

def recipe(request):
    recipes = Recipe.objects.all().values()
    paginator = Paginator(recipes, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        'recipes.html',
        {
            'title': 'Recipe',
            'message': 'Your application description page.',
            "page_obj": page_obj,
            "recipes": recipes
        })


def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Check if email is already taken
        if Client.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error': 'Email is already taken!'})

        # Check if passwords match
        if password1 != password2:
            return render(request, 'signup.html', {'error': 'Passwords do not match!'})

        # Create new user
        client = Client(email=email, password=password1)
        client.save()

        # Redirect to index page
        return redirect('login')

    # GET request
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            client = Client.objects.get(email=email, password=password)
            # set session variable to indicate that user is logged in
            request.session['client_id'] = client.id
            return redirect('index')
        except Client.DoesNotExist:
            # display error message
            error_message = 'Invalid email or password. Please try again.'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')


def migrate(request):
    fill_database()
def add_recipe(request):
    if request.method == 'POST':
        # Récupérer toutes les données du formulaire
        title = request.POST.get('title')
        description = request.POST.get('description')
        duration = request.POST.get('duration')  # Récupérer la durée depuis le formulaire
        nbrPersons = request.POST.get('nbrPersons')
        nbrCalories = request.POST.get('nbrCalories')
        difficulty = request.POST.get('difficulty')
        photo = request.FILES.get('photo')

        # Vérifier si la durée est renseignée
        if not duration:
            return render(request, 'add_recipe.html', {'error': 'Duration is required!'})

        # Créer une nouvelle instance de Recipe
        new_recipe = Recipe(
            title=title,
            description=description,
            duration=duration,
            nbrPersons=nbrPersons,
            nbrCalories=nbrCalories,
            difficulty=difficulty,
            imageUrl=photo
            # Ajouter d'autres champs ici selon votre modèle Recipe
        )

        # Sauvegarder la nouvelle recette dans la base de données
        new_recipe.save()

        # Rediriger vers une page (par exemple, la page des recettes)
        return redirect('recipes/')  # Mettez le nom de l'URL correspondant à la liste des recettes

    # Si la méthode HTTP n'est pas POST (par exemple, GET), afficher le formulaire
    return render(request, 'add_recipe.html')  # Créez un template pour le formulaire d'ajout de recette
