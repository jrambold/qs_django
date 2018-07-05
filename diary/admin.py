from django.contrib import admin

# Register your models here.
from .models import Food, Meal

admin.site.register(Food)
admin.site.register(Meal)
