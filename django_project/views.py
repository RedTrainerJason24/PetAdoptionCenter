from django.shortcuts import render
import django_project.main 

def home(request):
    return render(request, 'main.py')