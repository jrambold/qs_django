from django.urls import path

from . import views

urlpatterns = [
	path('foods', views.food_index, name='food_index'),
	path('foods/', views.food_index, name='food_index'),
	path('foods/<int:food_id>', views.food_show, name='food_show'),
	path('foods/<int:food_id>/', views.food_show, name='food_show'),
	path('meals', views.meal_index, name='meal_index'),
	path('meals/', views.meal_index, name='meal_index'),
	path('meals/<int:meal_id>/foods', views.meal_show, name='meal_show'),
	path('meals/<int:meal_id>/foods/', views.meal_show, name='meal_show'),
	path('meals/<int:meal_id>/foods/<int:food_id>', views.mf_show, name='mf_show'),
	path('meals/<int:meal_id>/foods/<int:food_id>/', views.mf_show, name='mf_show'),
]
