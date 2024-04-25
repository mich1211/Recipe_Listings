from django.db import models

# Create your models here.
def user_directory_path(instance, filename):
    return 'recipe_photos/{0}'.format(filename)

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    ingredients = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to=user_directory_path, null=True)

    def __str__(self):
        return self.title