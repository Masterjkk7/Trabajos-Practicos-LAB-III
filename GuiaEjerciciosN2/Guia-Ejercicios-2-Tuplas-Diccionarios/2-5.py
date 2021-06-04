def cargar():
    diccionario = {}
    for x in range(5):
        codigo = int(input("Ingrese el codigo de un producto: "))
        nombre = input("Ingrese su nombre: ")
        precio = int(input("Ingrese su precio: "))
        stock = int(input("Ingrese su stock: "))
        diccionario[codigo] = [nombre,precio,stock]
    
    return diccionario

def mostrar(diccionario):
    print(diccionario)

def busqueda(diccionario,palabra):
    if palabra in diccionario:
        print(palabra,":",diccionario[palabra])

def stock(diccionario):
    print("Productos con stock 0")
    for x in diccionario:
        if diccionario[x][2]==0:
            print(x,":",diccionario[x])

diccionario = cargar()
mostrar(diccionario)
codigo = int(input("Ingrese el codigo de un producto para buscar sus datos: "))
busqueda(diccionario,codigo)
stock(diccionario)

'''Confeccionar un programa que permita cargar un código de producto como
clave en un diccionario. Guardar para dicha clave el nombre del producto, su
precio y cantidad en stock.
Implementar las siguientes actividades:
1) Carga de datos en el diccionario.
2) Listado completo de productos.
3) Consulta de un producto por su clave, mostrar el nombre, precio y stock.
4) Listado de todos los productos que tengan un stock con valor cero.'''