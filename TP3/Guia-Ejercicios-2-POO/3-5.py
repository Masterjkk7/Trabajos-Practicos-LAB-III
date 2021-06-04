class Agenda():
    def __init__(self):
        self.contactos = []
    
    def __str__(self):
        cadena=str(self.contactos)
        return cadena
    
    def cargar(self):
        nombre = input("Ingrese el nombre del nuevo contacto: ")
        telefono = int(input("Ingrese el telefono del nuevo contacto: "))
        mail = input("Ingrese el mail del nuevo contacto: ")
        self.contactos.append([nombre,telefono,mail])
    
    def consulta(self):
        bool = False
        nombre = input("Ingrese el nombre del contacto a consultar: ")
        for x in self.contactos:
            if x[0] == nombre:
                print(x)
                bool = True
        if bool == False:
            print(nombre,"no se encuentra en la agenda.")
    
    def modificar(self):
        bool = False
        nombre = input("Ingrese el nombre del contacto a modificar: ")
        for x in self.contactos:
            if x[0] == nombre:
                print(x)
                bool = True
                x[1] = int(input("Ingrese el nuevo telefono: "))
                x[2] = input("Ingrese el nuevo mail: ")
        if bool == False:
            print(nombre,"no se encuentra en la agenda.")

a=Agenda()

opcion = 0

while opcion != 5:
    print('''1- Carga de un contacto en la agenda.
2- Listado completo de la agenda.
3- Consulta ingresando el nombre de la persona.
4- Modificación de su teléfono y mail.
5- Finalizar programa.''')
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        a.cargar()
    elif opcion == 2:
        print(a)
    elif opcion == 3:
        a.consulta()
    elif opcion == 4:
        a.modificar()
    elif opcion == 5:
        print("Cerrando el programa...")


'''Confeccionar una clase que administre una agenda personal. Se debe
almacenar el nombre de la persona, teléfono y mail. Debe mostrar un menú con
las siguientes opciones:
1- Carga de un contacto en la agenda.
2- Listado completo de la agenda.
3- Consulta ingresando el nombre de la persona.
4- Modificación de su teléfono y mail.
5- Finalizar programa.'''