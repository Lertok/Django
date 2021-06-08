from django.shortcuts import render


def products(request):
    title = 'каталог/продукты'

    links_menu = [
        {'href': 'mainapp:products', 'name': 'все'},
        {'href': 'mainapp:products', 'name': 'дом'},
        {'href': 'mainapp:products', 'name': 'офис'},
        {'href': 'mainapp:products', 'name': 'модерн'},
        {'href': 'mainapp:products', 'name': 'классика'},
    ]

    context = {
        'links_menu': links_menu,
        'title': title
    }

    return render(request, 'mainapp/products.html', context=context)
