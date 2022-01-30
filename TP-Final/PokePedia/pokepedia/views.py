import requests
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Pokemon

# Create your views here.

def get_pokemon(request: HttpRequest):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/rayquaza')
    """p = Pokemon()
    if response.status_code == 200:
        id = response.json()["id"]
        p.numero = id
        name = response.json()["name"]
        p.nombre = name
        ability = response.json()["abilities"][0]["ability"]["name"]
        p.habilidad = ability
        type1 = response.json()["types"][0]["type"]["name"]
        p.tipo.add(type1)
        type2 = response.json()["types"][1]["type"]["name"]
        p.tipo.add(type2)     
    context = {'pokemon': p}
    return render(request, 'pokepedia/search.html', context)"""
    return render(request, 'pokepedia/search.html')
