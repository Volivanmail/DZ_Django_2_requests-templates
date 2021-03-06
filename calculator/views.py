
from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def recipes_views (request, name):
    servings = request.GET.get('servings')
    lot = 1
    if servings:
        lot = int(servings)
    ingridients = DATA.get(name)
    ingridients.update({(x, y * lot) for x, y in ingridients.items()})
    context = {
        'ingredients': ingridients,
        'name': name,
        'servings': lot
    }
    return render(request, 'calculator/index.html', context=context)



# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
