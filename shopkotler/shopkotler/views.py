from django.shortcuts import render
from mainapp.models import Product

def index(request):
    title = 'shopkotler'
    products = Product.objects.all()[:4]

    context = {
        'products': products,
        'some_name': 'современные',
        'title': title,

    }
    return render(request, 'shopkotler/index.html', context=context)


def contact(request):
    title = 'контакты'

    context = {
        'title': title,
    }

    return render(request, 'shopkotler/contact.html', context=context)
