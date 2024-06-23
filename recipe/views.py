from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. Here is your Recipe: Water: Ingredients: Water 16oz")