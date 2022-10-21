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
    # можете добавить свои рецепты ;)
}


def omlet_view(request):
    context = {'recipe': DATA.get('omlet')}
    servings = int(request.GET.get('servings', 1))
    for key in context['recipe'].keys():
        context['recipe'][key] = context['recipe'][key] * servings
    return render(request, 'calculator/index.html', context=context)


def pasta_view(request):
    context = {'recipe': DATA.get('pasta')}
    servings = int(request.GET.get('servings', 1))
    for key in context['recipe'].keys():
        context['recipe'][key] = context['recipe'][key] * servings
    return render(request, 'calculator/index.html', context=context)


def buter_view(request):
    context = {'recipe': DATA['buter']}
    servings = int(request.GET.get('servings', 1))
    for key in context['recipe'].keys():
        context['recipe'][key] = context['recipe'][key] * servings
    return render(request, 'calculator/index.html', context=context)

