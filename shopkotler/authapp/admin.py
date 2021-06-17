from django.contrib import admin
from authapp.models import ShopUser

# Передали созданных пользователей
admin.site.register(ShopUser)
