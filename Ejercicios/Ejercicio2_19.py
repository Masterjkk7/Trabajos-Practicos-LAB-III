lista=[[4,12,5,66], [14,6,25], [3,4,5,67,89,23,1], [78,56]] 

print("Lista:",lista)

for x in lista:
    for y in x:
        if y > 10:
            x[x.index(y)] = 0

print("Lista nueva:",lista)

#2.19. Se tiene la siguiente lista: lista=[[4,12,5,66], [14,6,25], [3,4,5,67,89,23,1], [78,56]] 
#Imprimir la lista. Luego fijar con el valor cero todos los elementos mayores a 10 
#contenidos en todos los elementos de la variable "lista". Volver a imprimir la lista.