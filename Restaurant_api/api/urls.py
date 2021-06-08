from django.urls import path
from api.views import Restaurants, RestaurantDetail, Recipes, RecipeDetail

urlpatterns = [
    path('restaurants/', Restaurants.as_view()),
    path('restaurants/<str:restaurant_id>/', RestaurantDetail.as_view()),
    path('restaurants/<str:restaurant_id>/recipes/', Recipes.as_view()),
    path('restaurants/<str:restaurant_id>/recipes/<str:recipe_id>/', RecipeDetail.as_view())
]