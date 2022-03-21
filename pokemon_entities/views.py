import folium
from django.shortcuts import render, get_object_or_404
from pokemon_entities.models import Pokemon


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemons = Pokemon.objects.all()
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    pokemons_on_page = []

    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': request.build_absolute_uri(pokemon.picture.url),
            'title_ru': pokemon.title
        })

        pokemon_entities = pokemon.entities.all()

        for spec in pokemon_entities:
            add_pokemon(
                folium_map, spec.latitude,
                spec.longitude,
                request.build_absolute_uri(pokemon.picture.url)
            )

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)
    pokemon_entities = pokemon.entities.all()
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    next_pokemon = pokemon.next_evolution.all().first()

    for spec in pokemon_entities:
        add_pokemon(
            folium_map, spec.latitude,
            spec.longitude,
            request.build_absolute_uri(pokemon.picture.url)
        )

    pokemon_on_page = {
        'pokemon_id': pokemon.id,
        'img_url': request.build_absolute_uri(pokemon.picture.url),
        'title_ru': pokemon.title,
        'title_en': pokemon.title_en,
        'title_jp': pokemon.title_jp,
        'description': pokemon.description,
    }

    if pokemon.previous_evolution:
        pokemon_on_page['previous_evolution'] = {
            "title_ru": pokemon.previous_evolution,
            "pokemon_id": pokemon.previous_evolution_id,
            "img_url": request.build_absolute_uri(
                pokemon.previous_evolution.picture.url
            )
        }

    if next_pokemon:
        pokemon_on_page['next_evolution'] = {
                "title_ru": next_pokemon.title,
                "pokemon_id": next_pokemon.id,
                "img_url": request.build_absolute_uri(next_pokemon.picture.url)
            }

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon_on_page
    })
