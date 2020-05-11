from django.shortcuts import render
from recipes.models import RecipeItem, Author

def index(request):
    data = RecipeItem.objects.all()
    return render(request, "index.html", {"data": data})

def recipe_view(request, id):
    recipe = RecipeItem.objects.get(id=id)
    return render(request, "recipe.html", {"recipe": recipe})

def author_view(request, id):
    author = Author.objects.get(id=id)
    recipes = RecipeItem.objects.filter(author=author)
    return render(request, "bio.html", {"info": author, "recipes": recipes})
