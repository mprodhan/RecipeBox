from django.db import models

class Author(models.Model):
    name = models.CharField(max_length = 30)
    bio = models.TextField()

    def __str__(self):
        return self.name

class RecipeItem(models.Model):
    title = models.CharField(max_length = 20)
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    description = models.TextField()
    time_required = models.CharField(max_length = 20)
    instructions = models.TextField()

    def __str__(self):
        return f"{self.title} - {self.author}"