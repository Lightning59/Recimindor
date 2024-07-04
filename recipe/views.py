from django.shortcuts import render
from django.http import HttpResponse

from recipe.models import Recipe


# Create your views here.
def recipes(request):
    recipes_objs = Recipe.objects.all()
    context = {'recipes': recipes_objs}
    return render(request, 'recipe/recipes.html', context)