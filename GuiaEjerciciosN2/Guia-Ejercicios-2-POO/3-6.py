from random import *

class Dado():
    def __init__(self):
        self.valor = 0
    
    def tirar(self):
        self.valor = randrange(1,7)

    def __str__(self):
        cadena=str(self.valor)
        return cadena
    
    def retornar_valor(self):
        return self.valor

class JuegoDeDados():
    def __init__(self):
        self.dado1 = Dado()
        self.dado2 = Dado()
        self.dado3 = Dado()
    
    def jugar(self):
        print("Se tiran los dados...")
        self.dado1.tirar()
        self.dado2.tirar()
        self.dado3.tirar()

        print("Los dados muestran: ")
        print(self.dado1)
        print(self.dado2)
        print(self.dado3)

        if self.dado1.retornar_valor() == self.dado2.retornar_valor() and self.dado1.retornar_valor() == self.dado3.retornar_valor():
            print("Gano el juego")
        else:
            print("Perdio el juego")

jdd=JuegoDeDados()

opcion = 0

while opcion != 2:
    print("1) Jugar a los dados")
    print("2) Salir del programa")
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        jdd.jugar()
    elif opcion == 2:
        print("Cerrando el programa...")


'''Plantear un programa que permita jugar a los dados. Las reglas de juego
son: se tiran tres dados si los tres salen con el mismo valor mostrar un mensaje
que "gano", sino "perdió".
Pistas: Lo primero importar random. Despues lo que hacemos es
identificar las clases: Dado y JuegoDeDados. Luego los atributos y los
métodos de cada clase: 
#Clase Dado :
-atributos: valor
-métodos: tirar, imprimir, retornar_valor
#Clase JuegoDeDados:
-atributos: 3 Dado (3 objetos de la clase Dado)
-métodos: __init__, jugar'''