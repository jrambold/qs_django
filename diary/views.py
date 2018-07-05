from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from teams.models import Food, Meal
from django.core import serializers
import requests
import json
import os

# Create your views here.

def food_index(request):
    return JsonResponse({'Hello': 'World'})

def food_show(request):
    return JsonResponse({'Hello': 'World'})

def meal_index(request):
    return JsonResponse({'Hello': 'World'})

def meal_show(request):
    return JsonResponse({'Hello': 'World'})

def mf_show(request):
    return JsonResponse({'Hello': 'World'})
