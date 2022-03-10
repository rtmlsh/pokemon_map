from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=200, blank=True, verbose_name='Название покемона')
    title_en = models.CharField(max_length=200, blank=True, verbose_name='Название на английском')
    title_jp = models.CharField(max_length=200, blank=True, verbose_name='Название на япоском')
    description = models.TextField(blank=True, verbose_name='Описание покемона')
    picture = models.ImageField(upload_to='pokemons_images', null=True, verbose_name='Изображение')
    previous_evolution = models.ForeignKey('self', related_name='next_evolution', on_delete=models.CASCADE, verbose_name='Предыдущая эволюция', null=True, blank=True)

    def __str__(self):
        return f'{self.title}'


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, verbose_name='Покемон')
    longitude = models.FloatField(verbose_name='Долгота')
    latitude = models.FloatField(verbose_name='Широта')
    appeared_at = models.DateTimeField(verbose_name='Появился')
    disappeared_at = models.DateTimeField(verbose_name='Исчез')
    level = models.IntegerField(null=True, verbose_name='Уровень')
    health = models.IntegerField(null=True, verbose_name='Здоровье')
    attack = models.IntegerField(null=True, verbose_name='Атака')
    defense = models.IntegerField(null=True, verbose_name='Защита')
    stamina = models.IntegerField(null=True, verbose_name='Выносливость')

