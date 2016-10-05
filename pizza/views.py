from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from .models import Pizzas, Ingredients
from django.core import serializers
from pizza.serializer import PizzasSerializer
from rest_framework import viewsets


 
class ListPizzas(viewsets.ModelViewSet):
    """
    API endpoint that allows Pizzas to be viewed or edited.
    """
    queryset = Pizzas.objects.all()
    serializer_class = PizzasSerializer

