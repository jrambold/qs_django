from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from diary.models import Food, Meal
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json
import os

# Create your views here.

@csrf_exempt
def food_index(request):
    if request.method == 'GET':
    	foods = serializers.serialize("json", Food.objects.all())
    	return JsonResponse(json.loads(foods), safe=False)
    elif request.method == 'POST':
        try:
            food_data = json.loads(request.body)['food']
            food = Food(name = food_data['name'], calories = food_data['calories'])
            food.save()
        except:
            return HttpResponse('Bad Request', status=400)

        food = serializers.serialize("json", Food.objects.filter(id=food.id))
        return JsonResponse(json.loads(food), safe=False)

@csrf_exempt
def food_show(request, food_id):
    if request.method == 'GET':
        get_object_or_404(Food, pk=food_id)
        food = serializers.serialize("json", Food.objects.filter(id=food_id))
        return JsonResponse(json.loads(food), safe=False)

    elif request.method == 'PUT' or request.method == 'PATCH':
        try:
            food = Food.objects.get(pk=food_id)
        except Food.DoesNotExist:
            return HttpResponse('No Food matches that ID.', status=400)
        try:
            food_data = json.loads(request.body)['food']
            food.name = food_data['name']
            food.calories = food_data['calories']
            food.save()
        except:
            return HttpResponse('Bad Request', status=400)

        food = serializers.serialize("json", Food.objects.filter(id=food_id))
        return JsonResponse(json.loads(food), safe=False)

    elif request.method == 'DELETE':
        food = get_object_or_404(Food, pk=food_id)
        food.delete()
        return HttpResponse(status=204)

def meal_index(request):
    meals = serializers.serialize("json", Meal.objects.all())
    return JsonResponse(json.loads(meals), safe=False)

def meal_show(request, meal_id):
    get_object_or_404(Meal, pk=meal_id)
    meal = serializers.serialize("json", Meal.objects.filter(id=meal_id))
    return JsonResponse(json.loads(meal), safe=False)

@csrf_exempt
def mf_show(request, meal_id, food_id):
    if request.method == 'POST':
        food = get_object_or_404(Food, pk=food_id)
        meal = get_object_or_404(Meal, pk=meal_id)
        meal.foods.add(food)
        return JsonResponse({"message": f"Successfully added {food} to {meal}"}, status=201)

    elif request.method == 'DELETE':
        food = get_object_or_404(Food, pk=food_id)
        meal = get_object_or_404(Meal, pk=meal_id)
        meal.foods.remove(food)
        return JsonResponse({"message": f"Successfully removed {food} to {meal}"})
