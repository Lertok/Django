from django.shortcuts import render


def index(request):
    title = 'shopkotler'
    list_params = ['a1', 'a2', 'a3']

    context = {
        'list_params': list_params,
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
