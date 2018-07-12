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
        cereal = Food.objects.get(name="cereal")
        response = c.get(f"/api/v1/foods/{cereal.id}")
        food = json.loads(response.content)
        self.assertEqual(food['id'],cereal.id)
        self.assertEqual(food['name'],cereal.name)
        self.assertEqual(food['calories'],cereal.calories)

    def test_post_food(self):
        """Can post food endpoints"""
        c = Client()
        response = c.post('/api/v1/foods/', json.dumps({"food": { "name": "hello", "calories": "48"} }), content_type = "application/json")
        food = json.loads(response.content)
        hello = Food.objects.get(name="hello")
        self.assertEqual(int(food['id']),hello.id)
        self.assertEqual(food['name'],hello.name)
        self.assertEqual(int(food['calories']),hello.calories)

    def test_post_food_sad_path(self):
        """Can post bad request for no data"""
        c = Client()
        response = c.post('/api/v1/foods/')
        status = response.status_code
        self.assertEqual(status,400)

    def test_change_food(self):
        """Can put/patch food endpoints"""
        c = Client()
        response = c.post('/api/v1/foods/', json.dumps({"food": { "name": "world", "calories": "99"} }), content_type = "application/json")
        hello = Food.objects.get(name="world")

        self.assertEqual(hello.calories,99)

        response = c.patch(f"/api/v1/foods/{hello.id}", json.dumps({"food": { "name": "world", "calories": "101"} }), content_type = "application/json")
        food = json.loads(response.content)
        world = Food.objects.get(name="world")

        self.assertEqual(int(food['calories']),101)
        self.assertEqual(world.calories,101)

    def test_change_food_sad_path(self):
        """Can post bad request for no data"""
        c = Client()
        response = c.put('/api/v1/foods/1')
        status = response.status_code
        self.assertEqual(status,400)

    def test_delete_food(self):
        """Can put/patch food endpoints"""
        c = Client()
        response = c.post('/api/v1/foods/', json.dumps({"food": { "name": "thing", "calories": "99"} }), content_type = "application/json")
        hello = Food.objects.get(name="thing")
        response = c.delete(f"/api/v1/foods/{hello.id}")
        status = response.status_code
        self.assertEqual(status,204)

    def test_delete_food(self):
        """Can put/patch food endpoints"""
        c = Client()
        response = c.delete("/api/v1/foods/99")
        status = response.status_code
        self.assertEqual(status,404)

class MealEndPointCase(TestCase):
    def setUp(self):
        meal = Meal.objects.get(name="Breakfast")
        food = Food.objects.create(name="red", calories=12)
        food2 = Food.objects.create(name="green", calories=24)
        meal.foods.add(food)
        meal.foods.add(food2)

    def test_get_meals(self):
        """Can hit meals endpoints"""
        c = Client()
        response = c.get('/api/v1/meals/')
        foods = json.loads(response.content)
        self.assertEqual(len(foods), 4)
        self.assertEqual(foods[0]['name'],'Breakfast')
        self.assertEqual(len(foods[0]['foods']),2)

    def test_get_single_meal(self):
        """Can hit meals show endpoint"""
        c = Client()
        response = c.get('/api/v1/meals/1/foods')
        foods = json.loads(response.content)
        self.assertEqual(foods['name'],'Breakfast')
        self.assertEqual(len(foods['foods']),2)

    def test_post_meal_food(self):
        """Can post meal food endpoints"""
        c = Client()
        food = Food.objects.get(name="red")
        response = c.post(f"/api/v1/meals/1/foods/{food.id}")
        status = response.status_code
        self.assertEqual(status,201)
        meal = Meal.objects.get(id=1)
        self.assertEqual(len(meal.foods.all()),2)

    def test_post_meal_food_sad_path(self):
        """Can post meal food 404s endpoints"""
        c = Client()
        response = c.post(f"/api/v1/meals/1/foods/99")
        status = response.status_code
        self.assertEqual(status,404)

        response = c.post(f"/api/v1/meals/99/foods/2")
        status = response.status_code
        self.assertEqual(status,404)

    def test_delete_meal_food(self):
        """Can delete meal food endpoints"""
        c = Client()
        food = Food.objects.get(name="red")
        response = c.delete(f"/api/v1/meals/1/foods/{food.id}")
        meal = Meal.objects.get(id=1)
        self.assertEqual(len(meal.foods.all()),1)
        message = json.loads(response.content)
        self.assertEqual(message['message'],'Successfully removed red to Breakfast')


    def test_delete_meal_food_sad_path(self):
        """Can delete meal food 404s endpoints"""
        c = Client()
        response = c.post(f"/api/v1/meals/1/foods/99")
        status = response.status_code
        self.assertEqual(status,404)

        response = c.post(f"/api/v1/meals/99/foods/2")
        status = response.status_code
        self.assertEqual(status,404)
