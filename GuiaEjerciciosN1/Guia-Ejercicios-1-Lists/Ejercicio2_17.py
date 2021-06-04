l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10]
lista = [ l1, l2 ]

print("Lista principal:",lista)

for x in lista:
    suma = 0
    for y in x:
        suma = suma + y
    print("Suma de lista:",x,"=",suma)

#2.17. Crear una lista por asignación. La lista tiene que tener 2 elementos. 
# Cada elemento debe ser una lista de 5 enteros. 
# Calcular y mostrar la suma de cada lista contenida en la lista principal.