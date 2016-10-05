from django.contrib import admin

# Register your models here.
from .models import Ingredients, Pizzas

admin.site.register(Ingredients)
admin.site.register(Pizzas)