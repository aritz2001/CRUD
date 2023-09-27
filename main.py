import os   
import json

archivo = os.path.dirname(os.path.abspath(__file__))
fichero = os.path.join(archivo + '/bbdd/' 'base_datos.json')
def leer_json():
    with open(fichero,"r") as leer:
        datos = json.load(leer)
        leer.close()
        return datos
    
datos = leer_json()

class Persona(object):
    identificador = datos["Configuraciones"][0]["contador_id_bbdd"]
    def __init__(self, nombre, apellido, edad,telefono,direccion,email): #Creamos el constructor de la clase
        print("La posicion del contador es:", Persona.identificador)
        #Creamos las variables de instancia
        self.id = Persona.identificador 
        self.nombre = nombre
        self.apellido = apellido 
        self.edad = edad 
        self.telefono = telefono 
        self.direccion = direccion  
        self.email = email 

    def crear_persona(self):
        nueva_persona = {
            "id": len(datos["Personas"]) + 1,  # Generamos el ID de la personaa
            "nombre": self.nombre,
            "apellido": self.apellido,
            "edad": self.edad,
            "telefono": self.telefono,
            "direccion": self.direccion,
            "email": self.email
        }
        datos['Personas'].append(nueva_persona)
        for persona in datos["Personas"]:
            if "id" not in persona:
                persona["id"] = datos["Configuraciones"][0]["contador_id_bbdd"]
    
        with open(fichero, "w") as abrir:
            json.dump(datos, abrir, indent=4)
    
        print("El contador está ahora en: ", datos["Configuraciones"][0]["contador_id_bbdd"])
          
    def leer_persona(atr=None, valor=None): 
        resultados = {}
        for persona in datos["Personas"]:
            if (atr is None or valor is None) or (atr == "" and valor == ""):
                indice = datos["Personas"].index(persona)
                resultados[indice] = persona
            elif atr in persona and persona[atr] == valor:
                indice = datos["Personas"].index(persona)
                resultados[indice] = persona

        for index, persona in resultados.items():
            print(f'ID: {index}, Datos: {persona}')

    def modificar_persona(id, atr, datos_persona):
        for persona in datos["Personas"]:
            if persona["id"] == id:
                print("Antes de Modificarlo:", persona)
                persona[atr] = datos_persona
                print("Despues de modificarlo:", persona)
    
        with open(fichero, "w") as modificar:
            json.dump(datos, modificar, indent=4)

    def borrar_persona(id): #Creamos el metodo para borrar una persona
        for persona in datos["Personas"]:
            if persona["id"] == id:
                print("Se eliminara:", persona)
                datos["Personas"].remove(persona)
        with open(fichero, "w") as modificar:
            json.dump(datos, modificar, indent=4)

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
        print("Ha salido del programa")
        break