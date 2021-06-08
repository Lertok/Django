from django.urls import path
from .views import products


app_name = 'mainapp'


urlpatterns = [
    path('', products, name='products'),
    path('products/<int:pk>/', products, name='products'),
]
