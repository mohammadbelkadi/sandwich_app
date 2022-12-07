from django.shortcuts import render
from django.views import View
import random
# Create your views here.

ingredients = {
    'meats': ['turkey', 'beef', 'chicken'],
    'cheeses':['chedder', 'american', 'pepper jack'],
    'toppings':['onions', 'lettuce', 'peppers']
}

class SandwichappView(View):
    def get(self, request):
        return render (
            request = request,
            template_name = "sandwichapp.html",
            context = {'ingredients': ingredients.keys()}
        )

class IngredientsView(View):
    def get(self, request, ingredient_type):
        return render (
            request = request,
            template_name = "ingredients_list.html",
            context = {'ingredients': ingredients[ingredient_type],
            'ingredient_type': ingredient_type 
            }
        )

class RandomSandwichView(View):
    def get(self, request):
        return render (
            request = request,
            template_name = "random_sandwich.html",
            context = {
                'meats': random.choice(ingredients['meats']),
                'cheeses': random.choice(ingredients['cheeses']),
                'toppings': random.choice(ingredients['toppings']),
            }
        )
class MenuView(View):
    def get(self, request):
        menus = []
        for meat in ingredients['meats']:
            for cheese in ingredients['cheeses']:
                for topping in ingredients['toppings']:
                    sandwich=f'{meat} and {cheese} with {topping}'
                    menus.append(sandwich) 
        print(menus)
        return render ( 
            request,
            "menu.html",
            context = {
                'menus':menus
            }
        )