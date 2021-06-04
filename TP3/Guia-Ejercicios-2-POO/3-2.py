class Triangulo():
    def __init__(self, lado1:int, lado2:int, lado3:int):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def __str__(self):
        cadena=str(self.lado1)+" - "+str(self.lado2)+" - "+str(self.lado3)
        return cadena
    
    def mayor(self):
        lista = [self.lado1,self.lado2,self.lado3]
        return max(lista)
    
    def equilatero(self):
        bool = False
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            bool = True
        return bool

t1=Triangulo(10,10,10)
t2=Triangulo(9,6,3)
t3=Triangulo(4,8,4)

print(t1)
print(t2)
print(t3)

print("El lado mas grande del traingulo 1 es el",t1.mayor())
print("El lado mas grande del traingulo 2 es el",t2.mayor())
print("El lado mas grande del traingulo 3 es el",t3.mayor())

if t1.equilatero()==True:
    print("El Traingulo 1 es equilatero")
else:
    print("El Traingulo 1 no es equilatero")

if t2.equilatero()==True:
    print("El Traingulo 2 es equilatero")
else:
    print("El Traingulo 2 no es equilatero")

if t3.equilatero()==True:
    print("El Traingulo 3 es equilatero")
else:
    print("El Traingulo 3 no es equilatero")


'''Desarrollar un programa que cargue los lados de un triángulo e implemente
los siguientes métodos: inicializar los atributos, imprimir el valor del lado mayor y
otro método que muestre si es equilátero o no. El nombre de la clase llamarla
Triangulo.'''