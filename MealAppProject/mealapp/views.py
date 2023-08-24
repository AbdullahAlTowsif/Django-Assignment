from django.shortcuts import render
from .data import meals
# Create your views here.

def index(request):
    return render(request, './mealapp/index.html', {'meals': meals})
