from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from diary.models import Food, Meal
from django.core import serializers
import requests
import json
import os

# Create your views here.

def food_index(request):
	foods = serializers.serialize("json", Food.objects.all())
	return JsonResponse(json.loads(foods), safe=False)

def food_show(request, food_id):
	food = serializers.serialize("json", Food.objects.filter(id=food_id))
	return JsonResponse(json.loads(food), safe=False)

def meal_index(request):
    return JsonResponse({'Hello': 'World'})

def meal_show(request, meal_id):
    return JsonResponse({'Hello': 'World'})

def mf_show(request, meal_id, food_id):
    return JsonResponse({'Hello': 'World'})
