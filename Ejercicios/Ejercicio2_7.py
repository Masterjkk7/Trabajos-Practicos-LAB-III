lista = []
entero = -1

print("Ingrese 0 para dejar de ingresar numeros") 

while entero != 0:
    entero = int(input("Ingrese un numero entero:"))
    if entero !=0:
        lista.append(entero)

print("Enteros:",lista)

print("Esta lista tiene un tamaño de",len(lista))

#2.7. Realizar la carga de valores enteros por teclado, almacenarlos en una lista. 
#Finalizar la carga de enteros al ingresar el cero. Mostrar finalmente el tamaño de la lista.