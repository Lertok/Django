from django.db import models

# blank=True - позволяет оставлять поле незаполненным, null=True ставит null в то поле которое не заполнено, но должно.


class ProductCategory(models.Model):
    name = models.CharField(
        verbose_name='имя',
        max_length=64,
        unique=True,
    )

    description = models.TextField(
        verbose_name='описание',
        blank=True,
    )

    created = models.DateTimeField(
        auto_now_add=True,
    )

    updated = models.DateTimeField(
        auto_now=True,
    )

    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} - {self.id} -- {self.created}'

    class Meta: # для изменения названий
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

# decimal = models.DecimalField(max_digits=10, decimal_places=223) - используется для финансовых записей
# python manage.py makemigrations - пишем в терминале - передача(миграция) для базы
# python manage.py migrate - для применения файла


class Product(models.Model):
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        verbose_name='категория',
    )

    name = models.CharField(
        verbose_name='имя продукта',
        max_length=128,
    )

    image = models.ImageField(
        upload_to='products_images',
        blank=True,
        verbose_name='фото товара'
    )

    short_desc = models.CharField(
        verbose_name='краткое описание товара',
        max_length=60,
        blank=True,
    )

    description = models.TextField(
        verbose_name='описание продукта',
        blank=True,
    )

    price = models.DecimalField(
        verbose_name='цена продукта',
        max_digits=8,
        decimal_places=2,
        default=0,
    )

    quantity = models.PositiveIntegerField(
        verbose_name='количество на складе',
        default=0,
    )

    created = models.DateTimeField(
        auto_now_add=True,
    )

    updated = models.DateTimeField(
        auto_now=True,
    )

    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} - {self.id} -- {self.created}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'