from django.db import models

# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length=200)
    calories = models.IntegerField()

    def __str__(self):
        return self.name

class Meal(models.Model):
    name = models.CharField(max_length=200)
    foods = models.ManyToManyField(Food)

    def __str__(self):
        return self.name
