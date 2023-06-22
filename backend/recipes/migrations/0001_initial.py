# Generated by Django 3.2.16 on 2023-06-22 18:20

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'избранное',
                'verbose_name_plural': 'избранные',
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название ингредиента')),
                ('measurement_unit', models.CharField(max_length=10, verbose_name='Единица измерения ингредиента')),
            ],
            options={
                'verbose_name': 'Ингредиент',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название блюда')),
                ('text', models.CharField(max_length=10000, verbose_name='Описание блюда')),
                ('cooking_time', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Время приготовления блюда')),
                ('image', models.ImageField(upload_to='recipes/images/')),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
            },
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Ингредиент в рецепте',
            },
        ),
        migrations.CreateModel(
            name='RecipeTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Название тэга')),
                ('color', models.CharField(blank=True, max_length=7, validators=[django.core.validators.RegexValidator(message='Неподходящее название', regex='^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$')], verbose_name='Цвет тэга')),
                ('slug', models.SlugField(max_length=200, unique=True, validators=[django.core.validators.RegexValidator(message='Неподходящее название', regex='^[-a-zA-Z0-9_]+$')])),
            ],
            options={
                'verbose_name': 'Тэг',
            },
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shopping_cart', to='recipes.recipe', verbose_name='Покупки для рецепта')),
            ],
            options={
                'verbose_name': 'корзина для покупок',
                'verbose_name_plural': 'корзины для покупок',
            },
        ),
    ]
