import requests
import os
import plotly.express as px
from datetime import date
from settings import URL
from utils import getPaises


def main():
    os.system("cls")
    print("Este programa permite realizar un semaforo segun la cantidad de contagios en los paises del mundo")
    print("1) Generar un semaforo sobre un periodo de tiempo determinado")
    print("2) Generar un semaforo sobre toda la pandemia")
    print("3) Ver la URL y la cantidad de paises")
    opcion = input("Ingrese una opcion: ")
    os.system("cls")

    if opcion == "1":
        casos_pais = {}
        print("Ingrese la fecha en el siguiente formato: Año-Mes-Dia. Ejemplo: 2000-08-03")
        fecha_inicio = input("Fecha de  inicio del periodo: ")

        #Control 1
        if fecha_inicio < "2020-01-22":
            fecha_inicio = "2020-01-22"
            print("Fecha inicio = " + fecha_inicio)
    
        fecha_final = input("Fecha de  fin del periodo: ")

        #Control 2
        if fecha_final > date.today().strftime("%Y-%m-%d"):
            fecha_final = date.today().strftime("%Y-%m-%d")
            print("Fecha final = " + fecha_final)

        for pais in getPaises():
            url_periodo = f"https://api.covid19api.com/country/{pais}/status/confirmed?from={fecha_inicio}T00:00:00Z&to={fecha_final}T00:00:00Z"
            response = requests.get(url_periodo)
            if response.status_code == 200 and len(response.json()) >= 2:
                casos_inicio = []
                casos_final = []
                casos_inicio_total = 0
                casos_final_total = 0

                for dato in response.json():
                    if dato["Date"] == fecha_inicio + "T00:00:00Z":
                        casos_inicio.append(dato["Cases"])
                    if dato["Date"] == fecha_final + "T00:00:00Z":
                        casos_final.append(dato["Cases"])
                    print(dato["Country"] + ": " + str(dato["Cases"]))
                
                for x in range(len(casos_inicio)):
                    casos_inicio_total = casos_inicio_total + casos_inicio[x]
                for y in range(len(casos_final)):
                    casos_final_total = casos_final_total + casos_final[y]

                casos_pais[pais] = casos_final_total - casos_inicio_total
                casos_pais_ordenado = sorted(casos_pais.items(), key=lambda x: x[1], reverse=True)

        os.system("cls")
        print('\n')
        print("Paises y su cantidad de casos")
        print(casos_pais)
        print('\n')
        print("Paises ordenados por cantidad de casos")
        print(casos_pais_ordenado)

        paises = []
        for i in casos_pais_ordenado:
            paises.append(i[0])

        casos = []
        for i in casos_pais_ordenado:
            casos.append(i[1])

        rojo = []
        amarillo = []
        verde = []
        divisiones = int(len(casos_pais_ordenado) / 3)

        for x in range(divisiones):
            rojo.append(casos_pais_ordenado[x])

        for x in range(divisiones):
            amarillo.append(casos_pais_ordenado[divisiones + x])   

        for x in range(divisiones):
            verde.append(casos_pais_ordenado[(divisiones*2) + x])    

        colores = []
        for i in range(divisiones):
            colores.append("red")
        for j in range(divisiones):
            colores.append("yellow")
        for k in range(divisiones):
            colores.append("green")

        fig = px.bar(
            x=paises, 
            y=casos, 
            color=paises,
            color_discrete_sequence=colores,
            title="Semaforo de paises segun sus casos entre " + fecha_inicio + " y " + fecha_final,
            labels=dict(x="Pais", y="Casos", color="Pais")
            )
        fig.show()

        print('\n')
        print("Paises rojos")
        print(rojo)
        print('\n')
        print("Paises amarillos")
        print(amarillo)
        print('\n')
        print("Paises verdes")
        print(verde)         

    elif opcion == "2":
        casos_pais = {}
        url_global = "https://api.covid19api.com/summary"
        response = requests.get(url_global)
        if response.status_code == 200:
            for pais in response.json()["Countries"]:
                casos_pais[pais["Country"]] = pais["TotalConfirmed"]
                print(pais["Country"] + ": " + str(pais["TotalConfirmed"]))
            casos_pais_ordenado = sorted(casos_pais.items(), key=lambda x: x[1], reverse=True)
        
        os.system("cls")
        print('\n')
        print("Paises y su cantidad de casos")
        print(casos_pais)
        print('\n')
        print("Paises ordenados por cantidad de casos")
        print(casos_pais_ordenado)

        paises = []
        for i in casos_pais_ordenado:
            paises.append(i[0])

        casos = []
        for i in casos_pais_ordenado:
            casos.append(i[1])

        rojo = []
        amarillo = []
        verde = []
        divisiones = int(len(casos_pais_ordenado) / 3)

        for x in range(divisiones):
            rojo.append(casos_pais_ordenado[x])

        for x in range(divisiones):
            amarillo.append(casos_pais_ordenado[divisiones + x])   

        for x in range(divisiones):
            verde.append(casos_pais_ordenado[(divisiones*2) + x])    

        colores = []
        for i in range(divisiones):
            colores.append("red")
        for j in range(divisiones):
            colores.append("yellow")
        for k in range(divisiones):
            colores.append("green")

        fig = px.bar(
            x=paises, 
            y=casos, 
            color=paises,
            color_discrete_sequence=colores,
            title="Semaforo de paises segun sus casos en toda la pandemia",
            labels=dict(x="Pais", y="Casos", color="Pais")
            )
        fig.show()

        print('\n')
        print("Paises rojos")
        print(rojo)
        print('\n')
        print("Paises amarillos")
        print(amarillo)
        print('\n')
        print("Paises verdes")
        print(verde)
    
    elif opcion == "3":
        print(URL)
        print(len(getPaises()))

if __name__ == '__main__':
    main()
