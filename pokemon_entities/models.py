from django.db import models


class Pokemon(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название покемона',
        blank=True
    )
    title_en = models.CharField(
        max_length=200,
        verbose_name='Название на английском',
        blank=True
    )
    title_jp = models.CharField(
        max_length=200,
        verbose_name='Название на япоском',
        blank=True
    )
    description = models.TextField(
        verbose_name='Описание покемона',
        blank=True
    )
    picture = models.ImageField(
        upload_to='pokemons_images',
        verbose_name='Изображение',
        null=True
    )
    previous_evolution = models.ForeignKey(
        'self',
        related_name='next_evolution',
        on_delete=models.CASCADE,
        verbose_name='Предыдущая эволюция',
        null=True
    )

    def __str__(self):
        return f'{self.title}'


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE,
        verbose_name='Покемон',
        null=True
    )
    longitude = models.FloatField(verbose_name='Долгота', null=True)
    latitude = models.FloatField(verbose_name='Широта', null=True)
    appeared_at = models.DateTimeField(
        verbose_name='Появился',
        blank=True,
        null=True
    )
    disappeared_at = models.DateTimeField(
        verbose_name='Исчез',
        blank=True,
        null=True
    )
    level = models.IntegerField(verbose_name='Уровень', blank=True, null=True)
    health = models.IntegerField(
        verbose_name='Здоровье',
        blank=True,
        null=True
    )
    attack = models.IntegerField(verbose_name='Атака', blank=True, null=True)
    defense = models.IntegerField(verbose_name='Защита', blank=True, null=True)
    stamina = models.IntegerField(
        verbose_name='Выносливость',
        blank=True,
        null=True
    )
