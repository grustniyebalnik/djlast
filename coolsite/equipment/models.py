from django.db import models
from django.urls import reverse
class Equipment(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    price = models.IntegerField(verbose_name="Цена")
    content = models.TextField(blank=True, verbose_name="Описание")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="Фото")
    is_published = models.BooleanField(default=True, verbose_name="Наличие")
    time_create = models.DateTimeField(auto_now=True, verbose_name="Время создания")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name="Категория")
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('prod', kwargs={'prod_id': self.pk})

    class Meta:
        verbose_name = "Продукция/Товары"
        verbose_name_plural = "Продукция/Товары"
        ordering = ['time_create', 'title']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name="Категории"
        verbose_name_plural = "Категории"
        ordering = ['id']