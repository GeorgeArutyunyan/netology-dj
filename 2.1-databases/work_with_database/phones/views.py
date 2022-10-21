from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sorted_page = request.GET.get('sort', '')
    scope_phones = Phone.objects.all()

    if sorted_page == 'name':
        phones = scope_phones.order_by('name')
        context = {'phones': phones}
        return render(request, template, context)

    elif sorted_page == 'max_price':
        phones = scope_phones.order_by('-price')
        context = {'phones': phones}
        return render(request, template, context)

    elif sorted_page == 'min_price':
        phones = scope_phones.order_by('price')
        context = {'phones': phones}
        return render(request, template, context)

    context = {'phones': scope_phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phones = Phone.objects.get(slug=slug)
    context = {'phones': phones}
    return render(request, template, context)
