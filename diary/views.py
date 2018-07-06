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
        foods = list(Food.objects.all().values('id', 'name', 'calories'))
        return JsonResponse(foods, safe=False)
    elif request.method == 'POST':
        try:
            food_data = json.loads(request.body)['food']
            food = Food(name = food_data['name'], calories = food_data['calories'])
            food.save()
            return JsonResponse({'id':food.id, 'name':food.name, 'calories':food.calories})
        except:
            return HttpResponse('Bad Request', status=400)

@csrf_exempt
def food_show(request, food_id):
    if request.method == 'GET':
        food = get_object_or_404(Food, pk=food_id)
        return JsonResponse({'id':food.id, 'name':food.name, 'calories':food.calories})

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
            return JsonResponse({'id':food.id, 'name':food.name, 'calories':food.calories})
        except:
            return HttpResponse('Bad Request', status=400)

    elif request.method == 'DELETE':
        food = get_object_or_404(Food, pk=food_id)
        food.delete()
        return HttpResponse(status=204)

def meal_index(request):
    meal_list = []
    for meal in Meal.objects.all():
        food_list = list(meal.foods.values('id', 'name', 'calories'))
        meal_list.append({'id':meal.id, 'name':meal.name, 'foods':food_list})
    return JsonResponse(meal_list, safe=False)

def meal_show(request, meal_id):
    meal = get_object_or_404(Meal, pk=meal_id)
    food_list = list(meal.foods.values('id', 'name', 'calories'))
    return JsonResponse({'id':meal.id, 'name':meal.name, 'foods':food_list})

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
