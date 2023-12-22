from django.shortcuts import render, reverse

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
    # можете добавить свои рецепты ;)
}


def home(request):
    pages = {
        'Омлет': reverse('omlet'),
        'Паста': reverse('pasta'),
        'Бутер': reverse('buter'),
    }

    context = {
        'pages': pages
    }
    return render(request, 'calculator/home.html', context)


def omlet(request):
    servings = request.GET.get('servings', 1)
    context = {
        'recipe': {key: value * int(servings) for key, value in DATA['omlet'].items()}
    }
    return render(request, 'calculator/index.html', context)


def pasta(request):
    servings = request.GET.get('servings', 1)
    context = {
        'recipe': {key: value * int(servings) for key, value in DATA['pasta'].items()}
    }
    return render(request, 'calculator/index.html', context)


def buter(request):
    servings = request.GET.get('servings', 1)
    context = {
        'recipe': {key: value * int(servings) for key, value in DATA['buter'].items()}
    }
    return render(request, 'calculator/index.html', context)
