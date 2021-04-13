from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def admin(request):
    return render(request, "admin.html")