from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def recipes(request):
    return render(request, 'recipe/recipes.html')