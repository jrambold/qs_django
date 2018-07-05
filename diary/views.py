from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from diary.models import Food, Meal
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import requests
import json
import os

# Create your views here.

@csrf_exempt
def food_index(request):
    if request.method == 'GET':
    	foods = serializers.serialize("json", Food.objects.all())
    	return JsonResponse(json.loads(foods), safe=False)
    elif request.method == 'POST':
        food_data = json.loads(request.body)['food']
        food = Food(name = food_data['name'], calories = food_data['calories'])
        food.save()

        food = serializers.serialize("json", Food.objects.filter(id=food.id))
        return JsonResponse(json.loads(food), safe=False)

def food_show(request, food_id):
	food = serializers.serialize("json", Food.objects.filter(id=food_id))
	return JsonResponse(json.loads(food), safe=False)

def meal_index(request):
    meals = serializers.serialize("json", Meal.objects.all())
    return JsonResponse(json.loads(meals), safe=False)

def meal_show(request, meal_id):
    meal = serializers.serialize("json", Meal.objects.filter(id=meal_id))
    return JsonResponse(json.loads(meal), safe=False)

def mf_show(request, meal_id, food_id):
    return JsonResponse({'Hello': 'World'})
