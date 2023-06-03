from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
import django_project.test as t
import django_project.inventory as i
import django_project.email as email
#import django_project.password as p
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django_project.register import UserRegisterForm
from django_project.models import Pet
from django_project.models import Favorite
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



from django.contrib.auth.models import User
#import parser

def main(request):
    if request.method == 'GET':
        p = Pet.objects.all()
        #t.test()
        #return render(request, 'index.html')
        return render(request, 'Home.html', {'pet1': p[0], 'pet2': p[1], 'pet3': p[2]})

def signup(request):
    context = {}
    if request.method == 'GET':
        form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        print(request.POST)
        if form.is_valid():
          # username = request.POST['username']
          # email = request.POST['email']
          # password = request.POST['password']
          # user = User.objects.create_user(username, email, password)
          form.save()
          username = form.cleaned_data.get('username')
          raw_password = form.cleaned_data.get('password1')
          user = authenticate(username=username, password=raw_password)
          login(request, user)
          return redirect('home')
            #return render(request, 'login.html', context)
        else:
          print('Error registering')
    context.update(csrf(request))
    return render(request, 'signup.html', {'form': form, 'context': context})
  
def contactus(request):
    if request.method == 'GET':
        return render(request, 'contact.html')
    if request.method == 'POST':
        context = {}
        context.update(csrf(request))
        # INSERT START
        email.sendMail(request.POST)
        # INSERT END
        return render(request, 'contact.html', context)

def user_logout(request):
  if request.user.is_authenticated:
      logout(request)
  return redirect('home')

def user_login(request):
    form = AuthenticationForm()
    if request.method == 'POST' and not request.user.is_authenticated:
      form = AuthenticationForm(request=request, data=request.POST)
      if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        print(username + ' ' + password)
        user = authenticate(username=username, password=password)
        if user is not None:
          login(request, user)
          return redirect('home')  
        else:
          print('User not found.')
    return render(request, 'login.html', {'form': form})

        
def favorites(request):
     if not request.user.is_authenticated:
        return redirect('home')
     if request.method == 'GET':
        favorite_pets = Favorite.objects.all()
        pets = []
        for f in favorite_pets:
          if request.user == f.user:
            pets.append(f.pet)
          
        return render(request, 'favorites.html', {'data': pets})
    
def adoption(request):
    if request.method == 'GET':
        p = Pet.objects.all()
        for pets in p:
          pets.url = 'https://the-adoption-center.youknowhowtolov.repl.co/' + pets.name + '.html'
          pets.save()
        return render(request, "pet-adoption.html", {'data': p})
      
def adoption_search(request, search):
    if request.method == 'GET':
        p = Pet.objects.all()
        filtered = []
        for pets in p:
          if pets.species == search or pets.gender == search:
            filtered.append(pets)
          pets.url = 'https://the-adoption-center.youknowhowtolov.repl.co/' + pets.name + '.html'
          pets.save()
        return render(request, "pet-adoption.html", {'data': filtered})

def employee(request):
    if request.method == 'GET' and request.user.is_staff:
        p = Pet.objects.all()
        return render(request, "EmployeeOrginal.html", {'data': p})

    return redirect('home')

def barak(request):
  if request.method == 'GET':
      return render(request, "Barak-Obama-Info.html")

def milo(request):
  if request.method == 'GET':
      return render(request, "Milo-Info.html")

def snowballs(request):
  if request.method == 'GET':
      return render(request, "Snowballs-Info.html")

def sophia(request):
  if request.method == 'GET':
      return render(request, "Sophia-Info.html")

def vladimir(request):
  if request.method == 'GET':
      return render(request, "vladimir.html")

def barnie(request):
  if request.method == 'GET':
      return render(request, "barnie.html")

def reset(request):
  if request.method == 'GET':
      return render(request, "reset.html")


def newpass(request):
  if request.method == 'GET':
      return render(request, "newpass.html")
    

def upload(request):
    if not request.user.is_staff:
      return redirect('home')
    context = {}
    if request.method == 'POST':
        pet = Pet(name=request.POST['name'].rstrip(), age=request.POST['age'], species=request.POST['species'], breed=request.POST['breed'], gender=request.POST['gender'], description1=request.POST['description1'], description2=request.POST['description2'], description3=request.POST['description3'], image=request.FILES['image'])
        print(request.POST)
          # username = request.POST['username']
          # email = request.POST['email']
          # password = request.POST['password']
          # user = User.objects.create_user(username, email, password)
        pet.save()
          #return redirect('home')
            #return render(request, 'login.html', context)
     
    context.update(csrf(request))
    return render(request, 'upload.html', {'context': context})
    


def modify(request):
  if request.method == 'GET':
      return render(request, "modify.html")
  if request.method == 'POST':
      context = {}
      context.update(csrf(request))
      # INSERT START
      i.test(request)
      # INSERT END
        
      return render(request, 'upload.html', context)

def create_pet_html(request, pet_name):
    p = Pet.objects.all()
    all_favorites = Favorite.objects.all()
    has_already_favorited = {}
    for f in all_favorites:
      if request.user == f.user and f.pet.name == pet_name:
        has_already_favorited = f is not None
    for pets in p:
      if pets.name.lower() == pet_name.lower():
        return render(request, "pet-display.html", {'data': pets, 'favorited': has_already_favorited})
    #not found page
    return redirect('home')

def remove_pet(request, pet_name):
  if not request.user.is_staff:
      return redirect('home')
  all_pets = Pet.objects.all()
  for p in all_pets:
    if p.name == pet_name:
      p.delete()
      return redirect('employee')
        
def modify_pet(request, pet_name):
    if not request.user.is_staff:
      return redirect('home')
    if request.method == 'GET':
      p = Pet.objects.all()
      for pets in p:
        if pets.name.lower() == pet_name.lower():
          return render(request, "modify.html", {'data': pets})
    context = {}
    if request.method == 'POST':
        p = Pet.objects.get(name=pet_name)
        p.name=request.POST['name'].rstrip()
        p.age=request.POST['age'] 
        p.species=request.POST['species']
        p.breed=request.POST['breed']
        p.gender=request.POST['gender']
        p.description1=request.POST['description1']
        p.description2=request.POST['description2']
        p.description3=request.POST['description3']
        if 'image' in request.FILES and request.FILES['image']:
          p.image.delete(save=False)
          p.image=request.FILES['image']
        print(request.POST)
          # username = request.POST['username']
          # email = request.POST['email']
          # password = request.POST['password']
          # user = User.objects.create_user(username, email, password)
        p.save()
          #return redirect('home')
            #return render(request, 'login.html', context)
     
        context.update(csrf(request))
        #return render(request, 'upload.html', {'context': context})

    return render(request, "pet-display.html", {'data': p})

def favorite_pet(request, pet_name):
  if not request.user.is_authenticated:
      return redirect('home')
  user = User.objects.get(id=request.user)
  p = Pet.objects.get(name=pet_name)
  Favorite.objects.create(user=user, pet=p)
  create_pet_html(request, pet_name)

def favorite(request):
  p = Pet.objects.get(name=request.POST['pet'])
  if not request.user.is_authenticated or p is None:
      return redirect('home')
  #user = User.objects.get(id=request.user)
  #favorites = request.user.favorites.get(user=request.user, pet=p)
  try:
    valid_favorite = request.user.favorites.get(user=request.user, pet=p)
    if valid_favorite is not None:
      valid_favorite.delete()
  except:
    Favorite.objects.create(user=request.user, pet=p)
  return render(request, "pet-display.html", {'data': p})