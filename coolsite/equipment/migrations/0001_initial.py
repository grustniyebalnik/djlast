# Generated by Django 4.2.1 on 2023-05-30 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Категория')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категории',
                'verbose_name_plural': 'Категории',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('content', models.TextField(blank=True, verbose_name='Описание')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('is_published', models.BooleanField(default=True, verbose_name='Наличие')),
                ('time_create', models.DateTimeField(auto_now=True, verbose_name='Время создания')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='equipment.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Продукция/Товары',
                'verbose_name_plural': 'Продукция/Товары',
                'ordering': ['time_create', 'title'],
            },
        ),
    ]
