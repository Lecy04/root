from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "main/home.html")




def comparison(request):
    return render(request, 'main/comparison.html')

# Create your views here.
