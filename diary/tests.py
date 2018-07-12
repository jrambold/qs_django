from django.test import TestCase
from .models import Food, Meal
from django.test import Client
import json
# Create your tests here.

class FoodTestCase(TestCase):
    def setUp(self):
        Food.objects.create(name="taco", calories=12)
        Food.objects.create(name="pancake", calories=24)

    def test_animals_can_speak(self):
        """Foods are created"""
        taco = Food.objects.get(name="taco")
        pancake = Food.objects.get(name="pancake")
        self.assertEqual(taco.calories, 12)
        self.assertEqual(pancake.calories, 24)

class MealTestCase(TestCase):
    def setUp(self):
        meal = Meal.objects.create(name="brunch")
        food = Food.objects.create(name="casserole", calories=24)
        meal.foods.add(food)

    def test_meal_can_have_foods(self):
        """Meals can have foods"""
        brunch = Meal.objects.get(name="brunch")
        casserole = Food.objects.get(name="casserole")
        self.assertEqual(casserole.calories, 24)
        self.assertEqual(brunch.foods.get(name="casserole"), casserole)

class FoodEndPointCase(TestCase):
    def setUp(self):
        Food.objects.create(name="cereal", calories=12)
        Food.objects.create(name="milk", calories=24)

    def test_get_foods(self):
        """Can hit foods endpoints"""
        c = Client()
        response = c.get('/api/v1/foods/')
        foods = json.loads(response.content)
        self.assertEqual(len(foods), 2)
        self.assertEqual(foods[0]['name'],'cereal')
        self.assertEqual(foods[0]['calories'],12)
        self.assertEqual(foods[1]['name'],'milk')
        self.assertEqual(foods[1]['calories'],24)

    def test_get_food(self):
        """Can get single food endpoints"""
        c = Client()
        response = c.get('/api/v1/foods/1')
        food = json.loads(response.content)
        self.assertEqual(food['id'],1)
        self.assertEqual(food['name'],'cereal')
        self.assertEqual(food['calories'],12)

    def test_post_food(self):
        """Can post food endpoints"""
        c = Client()
        response = c.post('/api/v1/foods/', { "food": { "name": "hello", "calories": "48"} }, format='json')
        food = json.loads(response.content)
        hello = Food.objects.get(name="hello")
        self.assertEqual(food['id'],hello.id)
        self.assertEqual(food['name'],hello.name)
        self.assertEqual(food['calories'],hello.calories)
