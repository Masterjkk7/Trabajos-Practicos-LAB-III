from asyncio.windows_events import NULL
from ctypes.wintypes import BYTE
from re import X
from urllib.request import urlopen
import requests
from django.shortcuts import redirect, render
from .models import Pokemon, Tipo
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def main_page(request):
    return render(request, 'pokepedia/search.html')

def get_pokemon(request):
    try:        
        pokemon = request.POST.get('pokemon')
        try:
            try:
                x = Pokemon.objects.get(nombre__icontains=pokemon)
                print("El pokemon "+x.nombre+" ya esta registrado")
                context = {'pokemon' : x}
                return render(request, 'pokepedia/search.html', context)
            except ObjectDoesNotExist:
                x = Pokemon.objects.get(numero__icontains=pokemon)
                print("El pokemon "+x.nombre+" ya esta registrado")
                context = {'pokemon' : x}
                return render(request, 'pokepedia/search.html', context)
        except:
            response = requests.get('https://pokeapi.co/api/v2/pokemon/'+pokemon.lower())
            if response.status_code == 200:
                name = response.json()["name"]
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
                    print("Tipo 1: "+tipo1.nombre)
                except ObjectDoesNotExist:
                    print("El tipo "+type1+" no esta registrado")
                    t1 = Tipo.objects.create(nombre=type1.capitalize())
                    p.tipo.add(t1)

                try:
                    type2 = response.json()["types"][1]["type"]["name"]
                    try:
                        tipo2 = Tipo.objects.get(nombre__icontains=type2)
                        p.tipo.add(tipo2)
                        print("Tipo 2: "+tipo2.nombre)
                    except ObjectDoesNotExist:
                        print("El tipo "+type2+" no esta registrado")
                        t2 = Tipo.objects.create(nombre=type2.capitalize())
                        p.tipo.add(t2)
                except:
                    print("El pokemon "+name+" tiene un solo tipo")

                p.save()
                x = Pokemon.objects.latest('id')
                print("Indice de la tabla: "+str(x.id))
                context = {'pokemon' : x}
                print("Se registro el pokemon en la base de datos") 
                return render(request, 'pokepedia/search.html', context)
            else:
                print("ERROR API")
                context = {'error_api' : "error_api"}
                return render(request, 'pokepedia/search.html', context)
    except:
        print("ERROR POST")
        context = {'error_post' : "error_post"}
        return render(request, 'pokepedia/search.html', context)

#requests.exceptions.RequestException as e:
#raise SystemExit(e)
#return redirect('http://127.0.0.1:8000/admin/pokepedia/pokemon/'+str(x.id)+'/change/')