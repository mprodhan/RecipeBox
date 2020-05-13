from django.shortcuts import render, reverse, HttpResponseRedirect, HttpResponse
from recipes.models import RecipeItem, Author
from recipes.forms import RecipesAddForm, AuthorAddForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

def loginview(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data["username"],
                password=data["password"]
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse("homepage"))
                )
    form = LoginForm()
    return render(request, "generic_form.html", {"form": form})

def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))

def index(request):
    data = RecipeItem.objects.all()
    return render(request, "index.html", {"data": data})

@login_required
def recipesadd(request):
    html = "generic_form.html"
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

@login_required
def authoradd(request):
    html = "generic_form.html"
    if not request.user.is_staff:
        return HttpResponse("Sorry buddy Admin only privileges!")
    if request.method == "POST":
        form = AuthorAddForm(request.POST)
        new_author = form.save(commit=False)
        user = User.objects.create_user(username = new_author.name, password = "Bienvenue")
        new_author.User = user
        new_author.save()
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
