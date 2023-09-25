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

#def modificar_json():
#    with open(fichero,"r") as alterar:
 #       json.dump(datos, alterar, indent=4)
  #      alterar.close()

class Persona(object):
    identificador = datos["Configuraciones"][0]["contador_id_bbdd"]
    def __init__(self, nombre, apellido, edad,telefono,direccion,email): #Creamos el constructor de la clase
        print("La posicion del contador es:", Persona.identificador)
        self.id = Persona.identificador #Creamos la variable de instancia del identificador de la persona 
        self.nombre = nombre #Creamos la variable de instancia del nombre de la persona 
        self.apellido = apellido #Creamos la variable de instancia del apellido de la persona 
        self.edad = edad #Creamos la variable de instancia de la edad de la persona 
        self.telefono = telefono #Creamos la variable de instancia del telefono de la persona 
        self.direccion = direccion  #Creamos la variable de instancia  de la  dirección persona 
        self.email = email #Creamos la variable de instancia  del email de la persona 

    def crear_persona(self):
        nueva_persona = {
            "id": len(datos["Personas"]) + 1,  # Generate a unique ID for the new person
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
            if (atr is None or valor is None) or (atr == "all" and valor == "all"):
            # If both atr and valor are None or "all," show all records.
                indice = datos["Personas"].index(persona)
                resultados[indice] = persona
            elif atr in persona and persona[atr] == valor:
                # If atr matches and the value matches, add to results.
                indice = datos["Personas"].index(persona)
                resultados[indice] = persona

        for index, persona in resultados.items():
            print(f'ID: {index}, Datos: {persona}')

    def modificar_persona(id, atr, datos_persona):
        for persona in datos["Personas"]:
            if persona["id"] == id:
                print("Before modification:", persona)
                persona[atr] = datos_persona
                print("After modification:", persona)
    
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
    variable = int(input(print("Que deseas hacer? 1- Crear una persona \n 2- Leer el fichero \n 3-Modificar a una persona \n 4- Borrar una persona \n 5- Salir")))

    if variable == 1:
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        edad = int(input("Ingrese su edad: "))
        telefono = int(input("Ingrese su telefono: "))
        direccion = input("Ingrese su direccion: ")
        email = input("Ingrese su email: ")
        Persona(nombre, apellido, edad,telefono,direccion,email).crear_persona()
    elif variable == 2:
        atr = input("Ingrese el atributo a filtrar (o 'all' para mostrar todo): ")
        valor = input("Ingrese el valor del atributo (o 'all'): ")
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