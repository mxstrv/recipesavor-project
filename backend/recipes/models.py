from django.core.validators import RegexValidator, MinValueValidator
from django.db import models
from django.db.models import UniqueConstraint

from users.models import CustomUser


class Tag(models.Model):
    """ Модель тэгов для рецептов."""
    name = models.CharField(
        'Название тэга',
        max_length=200,
        blank=False,
        unique=True,
    )
    color = models.CharField(
        'Цвет тэга',
        max_length=7,
        unique=False,
        blank=True,
        validators=[RegexValidator(
            regex=r"^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$",
            message='Неподходящее название'), ]
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        validators=[RegexValidator(
            regex=r'^[-a-zA-Z0-9_]+$',
            message='Неподходящее название'), ]
    )

    class Meta:
        verbose_name = 'Тэг'

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """ Модель для ингредиента. """
    name = models.CharField(
        'Название ингредиента',
        max_length=150)
    measurement_unit = models.CharField(
        'Единица измерения ингредиента',
        max_length=10
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Ингредиент'
        constraints = [
            UniqueConstraint(
                fields=['name', 'measurement_unit'],
                name='ingredient_name_unit_unique'
            )
        ]


class Recipe(models.Model):
    """ Модель для рецептов."""
    name = models.CharField('Название блюда',
                            max_length=200,
                            blank=False, )
    text = models.CharField('Описание блюда',
                            max_length=10000,  # TODO CHECK SIZE
                            blank=False)
    cooking_time = models.IntegerField('Время приготовления блюда',
                                       blank=False,
                                       validators=[MinValueValidator(1), ])

    image = models.ImageField(
        upload_to='recipes/images/',
        blank=False,
        null=False,
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Автор рецепта'
    )
    tags = models.ManyToManyField(
        Tag,
        through='RecipeTag',
        related_name='tags'
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through='RecipeIngredient',
    )

    class Meta:
        verbose_name = 'Рецепт'

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
    )
    amount = models.IntegerField()

    class Meta:
        verbose_name = 'Ингредиент в рецепте'
        constraints = [
            UniqueConstraint(
                fields=['recipe', 'ingredient'],
                name='recipe_ingredient_unique'
            )
        ]


class RecipeTag(models.Model):
    """ Модель связи тега и рецепта. """

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт'
    )
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        verbose_name='Тег'
    )

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['recipe', 'tag'],
                name='recipe_tag_unique'
            )
        ]
