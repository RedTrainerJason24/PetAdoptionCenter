from django.contrib import admin
   
# Register your models here.
from django_project.models import Pet, Favorite
   
admin.site.register(Pet)
admin.site.register(Favorite)