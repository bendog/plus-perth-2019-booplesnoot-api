from django.shortcuts import render
import requests


def IndexView(request):
    url = 'https://api.spoonacular.com/recipes/search?apiKey=3dc537f85d054e38a4caadd57f887609&number=5'
    
    r = requests.get(url.format()).json()
    # r is short for response

    recipe_list = {
        'title' : r['results'][4]['title'],
        'image' : r['results'][4]['image'],
        'servings': r['results'][4]['servings'],
        'time' : r['results'][4]['readyInMinutes'],
    }

    context = {'recipe_list' : recipe_list}

    return render(request, 'recipefinderApp/recipefinder.html', context)

