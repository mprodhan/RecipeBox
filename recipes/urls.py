from django.urls import path
from recipes import views


urlpatterns = [
    path('', views.index, name= "homepage"),
    path('recipesadd/', views.recipesadd),
    path('authoradd/', views.authoradd),
    path('recipe/<int:id>/', views.recipe_view),
    path('author/<int:id>/', views.author_view),
    path('login/', views.loginview)
]

