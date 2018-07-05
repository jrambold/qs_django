from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from diary.models import Food, Meal
from django.core import serializers
import requests
import json
import os

# Create your views here.

def food_index(request):
	data = serializers.serialize("json", Food.objects.all())
	r = json.loads(data)
	return JsonResponse(r, safe=False)

def food_show(request):
    return JsonResponse({'Hello': 'World'})

def meal_index(request):
    return JsonResponse({'Hello': 'World'})

def meal_show(request):
    return JsonResponse({'Hello': 'World'})

def mf_show(request):
    return JsonResponse({'Hello': 'World'})
