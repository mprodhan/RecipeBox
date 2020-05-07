from django.shortcuts import render
from recipes.models import RecipeItem

def index(request):
    data = RecipeItem.objects.all()
    return render(request, "index.html", {"data": data})

def recipe(request):
    ingredients = RecipeItem.objects.all()
    return render(request, "recipe.html", {"recipe": ingredients})
