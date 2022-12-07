from django.urls import path
from sandwichapp.views import SandwichappView, IngredientsView, RandomSandwichView, MenuView 

urlpatterns = [
    path('', SandwichappView.as_view(), name='sandwich'),
    path('ingredients/<str:ingredient_type>', IngredientsView.as_view(), name = "ingredients_list"),
    path('random/', RandomSandwichView.as_view(), name='random_sandwich'),
    path('menu/', MenuView.as_view(), name = 'menu'),
    ]


    