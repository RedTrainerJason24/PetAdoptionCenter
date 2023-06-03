"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import main
from django.views.generic.list import ListView
from django_project.models import Pet

urlpatterns = [
    path('admin', admin.site.urls),
    path('', main.main, name='home'),
    path('contactus', main.contactus),
    path('login', main.user_login, name='login'),
    path('logout', main.user_logout, name='logout'),
    path('signup', main.signup),
    path('favorites', main.favorites),
    path('adoption', main.adoption),
    path('adoption/<search>', main.adoption_search),
    path('Employee', main.employee, name='employee'),
    path('Barak-Obama-Info', main.barak),
    path('Milo-Info', main.milo),
    path('Snowballs-Info', main.snowballs),
    path('Sophia-Info', main.sophia),
    path('vladimir.html', main.vladimir),
    path('barnie.html', main.barnie),
    path('reset', main.reset),
    path('newpass', main.newpass),
    path('upload', main.upload),
    path('modify', main.modify),
    path('modify/<pet_name>', main.modify_pet),
    path('remove/<pet_name>', main.remove_pet),
    path('favorite/<pet_name>', main.favorite_pet),
    path('favorite', main.favorite, name='favorite'),
    path('<pet_name>', main.create_pet_html),
   # path('indexEMPLOYEE', main.indexEmployee)
  
]



