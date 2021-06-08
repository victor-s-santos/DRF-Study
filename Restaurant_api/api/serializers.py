import os
import base64
from rest_framework import serializers
from .models import Restaurant, Recipe, Ingredient
from django.conf import settings

class RestaurantSerializer(serializers.ModelSerializer):
    """Serializer for the Restaurant model"""

    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'direction', 'phone']


class IngredientSerializer(serializers.ModelSerializer):
    """Serializer for the Ingredient model"""

    class Meta:
        model = Ingredient
        fields = ['id', 'name']


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for the Recipe model. 
    Using encode_thumbnail to handle the image"""

    thumbnail = serializers.SerializerMethodField('encode_thumbnail')
    ingredients = serializers.SerializerMethodField('get_ingredients')

    def encode_thumbnail(self, recipe):
        with open(os.path.join(settings.MEDIA_ROOT, recipe.thumbnail.name), "rb") as image:
            return base64.b64encode(image.read())

    def get_ingredients(self, recipe):
        try:
            recipe_ingredients = models.Ingredient.objects.filter(recipe__id=recipe.id)
            return IngredientSerializer(recipe_ingredients, many=True).data
        except models.Ingredient.DoesNotExist:
            return None

        def create(self, validated_data):
            """
            Create function for recipes, a restaurant and a list of ingredients is asociated. The restaurantId
            is taken from the corresponding path parameter and the ingredients can be added optionally in the post body.
            """
            ingredients_data = validated_data.pop("ingredients")
            restaurant = models.Restaurant.objects.get(pk=validated_data["restaurant_id"])
            validated_data["restaurant"] = restaurant
            recipe = models.Recipe.objects.create(**validated_data)

            """Assign ingredients if it are present in the body"""
            if ingredients_data:
                for ingredient_dict in ingredients_data:
                    ingredient = models.Ingredient(name=ingredient_dict["name"])
                    ingredient.save()
                    ingredient.recipe.add(recipe)
            return recipe
    
        class Meta:
            model = Recipe
            fields = ['id', 'name', 'type', 'thumbnail', 'ingredients'] 