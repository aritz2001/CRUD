from persona import Persona

while True:
    variable = int(input("Que deseas hacer?\n 1- Crear una persona \n 2- Leer el fichero \n 3-Modificar a una persona \n 4- Borrar una persona \n 5- Salir \n"))

    if variable == 1:
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        edad = int(input("Ingrese su edad: "))
        telefono = int(input("Ingrese su telefono: "))
        direccion = input("Ingrese su direccion: ")
        email = input("Ingrese su email: ")
        Persona(nombre, apellido, edad,telefono,direccion,email).crear_persona()
    elif variable == 2:
        atr = ""
        valor = ""
        Persona.leer_persona(atr,valor)
    elif variable == 3:
        id = int(input("Ingrese el id a modificar: "))
        atr = input("Ingrese el atributo a modificar (nombre, apellido, edad, telefono, direccion, email): ")
        valor = input(f"Ingrese el nuevo valor para {atr}: ")
        Persona.modificar_persona(id,atr,valor)
    elif variable == 4:
        id = int(input("Ingrese el id a borrar: "))
        Persona.borrar_persona(id)
    elif variable >= 5 or variable == 0:
        print("Has salido del programa")
        break