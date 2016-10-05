#from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Pizzas, Ingredients

class IngredientsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredients
        fields = ('name', 'price')

class PizzasSerializer(serializers.ModelSerializer):

    ingredients = IngredientsSerializer(many=True)

    class Meta:
        model = Pizzas
        fields = ('name', 'image', 'ingredients', 'prices')
