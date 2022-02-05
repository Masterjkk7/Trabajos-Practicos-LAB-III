from asyncio.windows_events import NULL
from ctypes.wintypes import BYTE
from io import BytesIO
from re import X
from urllib.request import urlopen
from django.forms import ImageField
import requests
from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from .models import Pokemon, Tipo
from django.core.exceptions import ObjectDoesNotExist
from PIL import Image

# Create your views here.

def main_page(request):
    return render(request, 'pokepedia/search.html')

def get_pokemon(request: HttpRequest):
    try:
        pokemon_name = request.POST.get('pokemon_name')
        response = requests.get('https://pokeapi.co/api/v2/pokemon/'+pokemon_name.lower())
        if response.status_code == 200:
            name = response.json()["name"]
            try:
                x = Pokemon.objects.get(nombre__icontains=name)
                print(x)
                context = context = {'pokemon' : x}
            except ObjectDoesNotExist:
                print("El pokemon "+name+" no esta registrado")
                id = response.json()["id"]
                ability = response.json()["abilities"][0]["ability"]["name"]

                p = Pokemon()
                p.numero = id
                p.nombre = name.capitalize()
                p.habilidad = ability.capitalize()

                img_route = 'sprites/'+str(id).zfill(3)+'.png'
                img = open('media/'+img_route, 'wb')
                img.write(urlopen('https://assets.pokemon.com/assets/cms2/img/pokedex/full/'+str(id).zfill(3)+'.png').read())
                img.close()
                
                p.apariencia = img_route
                p.save()

                type1 = response.json()["types"][0]["type"]["name"]
                try:
                    tipo1 = Tipo.objects.get(nombre__icontains=type1)
                    p.tipo.add(tipo1)
                    print(tipo1)
                except ObjectDoesNotExist:
                    print("El tipo "+type1+" no esta registrado")
                    t1 = Tipo.objects.create(nombre=type1.capitalize())
                    p.tipo.add(t1)

                try:
                    type2 = response.json()["types"][1]["type"]["name"]
                    try:
                        tipo2 = Tipo.objects.get(nombre__icontains=type2)
                        p.tipo.add(tipo2)
                        print(tipo2)
                    except ObjectDoesNotExist:
                        print("El tipo "+type2+" no esta registrado")
                        t2 = Tipo.objects.create(nombre=type2.capitalize())
                        p.tipo.add(t2)
                except:
                    print("El pokemon "+name+" tiene un solo tipo")

                p.save()
                x = Pokemon.objects.latest('id')
                print(x.id)
                context = {'pokemon' : x}
                return render(request, 'pokepedia/search.html', context) 
            return render(request, 'pokepedia/search.html', context)
            #return redirect('http://127.0.0.1:8000/admin/pokepedia/pokemon/'+str(x.id)+'/change/')
        else:
            return redirect('http://127.0.0.1:8000/')
    except requests.exceptions.RequestException as e:
        #raise SystemExit(e)
        return redirect('http://127.0.0.1:8000/') 
    
