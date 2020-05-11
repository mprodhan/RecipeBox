from django.shortcuts import render, reverse, HttpResponseRedirect
from recipes.models import RecipeItem, Author
from recipes.forms import RecipesAddForm, AuthorAddForm

def index(request):
    data = RecipeItem.objects.all()
    return render(request, "index.html", {"data": data})

def recipesadd(request):
    html = "recipesadd.html"
    if request.method == "POST":
        form = RecipesAddForm(request.POST)
        if form.is_valid():
            recipe = form.cleaned_data
            RecipeItem.objects.create(
                title = recipe['title'],
                description = recipe['description'],
                author = recipe['author']
            )
            return HttpResponseRedirect(reverse("homepage"))
    form = RecipesAddForm()
    return render(request, html, {"form": form})

def authoradd(request):
    html = "authoradd.html"
    if request.method == "POST":
        form = AuthorAddForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse("homepage"))
    form = AuthorAddForm()
    return render(request, html, {"form": form})


def recipe_view(request, id):
    recipe = RecipeItem.objects.get(id=id)
    return render(request, "recipe.html", {"recipe": recipe})

def author_view(request, id):
    author = Author.objects.get(id=id)
    recipes = RecipeItem.objects.filter(author=author)
    return render(request, "bio.html", {"info": author, "recipes": recipes})
