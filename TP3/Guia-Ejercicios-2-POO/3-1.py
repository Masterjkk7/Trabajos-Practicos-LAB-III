class Alumno():
    def __init__(self, nombre:str, nota:int):
        self.nombre = nombre
        self.nota = nota
    
    def __str__(self):
        cadena=self.nombre+" = "+str(self.nota)
        return cadena
    
    def regular(self):
        bool = True
        if self.nota<4:
            bool = False
        return bool

a1=Alumno("Franco Geremia",10)
a2=Alumno("Facundo Facello",4)
a3=Alumno("Hulk",2)

print(a1)
print(a2)
print(a3)

if a1.regular()==True:
    print("El alumno",a1.nombre,"esta aprobado con",a1.nota)
else:
    print("El alumno",a1.nombre,"esta desaprobado con",a1.nota)

if a2.regular()==True:
    print("El alumno",a2.nombre,"esta aprobado con",a2.nota)
else:
    print("El alumno",a2.nombre,"esta desaprobado con",a2.nota)

if a3.regular()==True:
    print("El alumno",a3.nombre,"esta aprobado con",a3.nota)
else:
    print("El alumno",a3.nombre,"esta desaprobado con",a3.nota)


'''Implementar una clase llamada Alumno que tenga como atributos su nombre
y su nota. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar
un mensaje si está regular (nota mayor o igual a 4)'''