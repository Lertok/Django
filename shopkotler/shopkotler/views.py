from django.shortcuts import render

from basketapp.models import Basket
from mainapp.models import Product


def index(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    title = 'shopkotler'
    products = Product.objects.all()[:4]

    context = {
        'products': products,
        'some_name': 'современные',
        'title': title,
        'basket': basket,

    }
    return render(request, 'shopkotler/index.html', context=context)


def contact(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    title = 'контакты'

    context = {
        'title': title,
        'basket': basket,
    }

    return render(request, 'shopkotler/contact.html', context=context)
