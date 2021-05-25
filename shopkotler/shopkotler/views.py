from django.shortcuts import render


def index(request):
    return render(request, 'shopkotler/index.html')

def contacts(request):
    return render(request, 'shopkotler/contact.html')
