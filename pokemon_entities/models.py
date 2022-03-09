from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=200, blank=True)
    title_en = models.CharField(max_length=200, blank=True)
    title_jp = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    picture = models.ImageField(upload_to='pokemons_images', null=True)
    evolution = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    next_evolution = models.ForeignKey('self', on_delete=models.CASCADE, related_name='evolution+', null=True, blank=True)

    def __str__(self):
        return f'{self.title}'


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    longitude = models.FloatField()
    latitude = models.FloatField()
    appeared_at = models.DateTimeField()
    disappeared_at = models.DateTimeField()
    level = models.IntegerField(null=True)
    health = models.IntegerField(null=True)
    attack = models.IntegerField(null=True)
    defense = models.IntegerField(null=True)
    stamina = models.IntegerField(null=True)

