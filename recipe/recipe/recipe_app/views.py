# Create your views here.
from django.shortcuts import render, redirect
from .models import Recipe

def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes': recipes})

def upload_recipe(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        ingredients = request.POST.get('ingredients')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        Recipe.objects.create(title=title, ingredients=ingredients, description=description, image=image)
        return redirect('index')
    return render(request, 'uploads.html')

