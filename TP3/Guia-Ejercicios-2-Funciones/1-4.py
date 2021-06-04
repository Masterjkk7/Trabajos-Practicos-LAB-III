def perimetro(lado):
    print("Perimetro:",(lado*4))

def area(lado):
    print("Area:",(lado*lado))

lado = int(input("Ingrese el lado de un cuadrado: "))

print("1) Calcular Perimetro")
print("2) Calcular Area")
opcion = int(input("Ingrese una opcion: "))

if opcion==1:
    perimetro(lado)
elif opcion==2:
    area(lado)

'''Desarrollar un programa que permita ingresar el lado de un cuadrado. Luego
preguntar si quiere calcular y mostrar su perímetro o su superficie.'''