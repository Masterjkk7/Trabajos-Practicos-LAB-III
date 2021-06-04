class Empleado():
    def __init__(self):
        self.nombre = input("Ingrese el nombre del empleado: ")
        self.sueldo = int(input("Ingrese el sueldo del empleado: "))
    
    def __str__(self):
        cadena=self.nombre+" = "+str(self.sueldo)
        return cadena
    
    def impuestos(self):
        bool = False
        if self.sueldo>3000:
            bool = True
        return bool

e1=Empleado()
e2=Empleado()
e3=Empleado()

print(e1)
print(e2)
print(e3)

if e1.impuestos()==True:
    print("El Empleado",e1.nombre,"debe pagar impuestos")
else:
    print("El Empleado",e1.nombre,"no debe pagar impuestos")

if e2.impuestos()==True:
    print("El Empleado",e2.nombre,"debe pagar impuestos")
else:
    print("El Empleado",e2.nombre,"no debe pagar impuestos")

if e3.impuestos()==True:
    print("El Empleado",e3.nombre,"debe pagar impuestos")
else:
    print("El Empleado",e3.nombre,"no debe pagar impuestos")


'''Confeccionar una clase que represente un empleado. Definir como atributos
su nombre y su sueldo. En el método __init__ cargar los atributos por teclado y
luego en otro método imprimir sus datos y por último uno que imprima un
mensaje si debe pagar impuestos (si el sueldo supera a 3000).'''