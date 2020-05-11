from django.urls import path
from recipes import views


urlpatterns = [
    path('', views.index),
    path('recipe/<int:id>/', views.recipe_view),
    path('author/<int:id>/', views.author_view)
]

