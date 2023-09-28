from datos import datos2
import json 

informacion = datos2()
informacion.leer_json()
class Persona(object):
    identificador = informacion.datos["Configuraciones"][0]["contador_id_bbdd"]
    def __init__(self, nombre, apellido, edad,telefono,direccion,email): #Creamos el constructor de la clase
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
            "id": len(informacion.datos["Personas"]) + 1,  # Generamos el nuevo ID de la personaa
            "nombre": self.nombre,
            "apellido": self.apellido,
            "edad": self.edad,
            "telefono": self.telefono,
            "direccion": self.direccion,
            "email": self.email
        }
        informacion.datos['Personas'].append(nueva_persona)
        for persona in informacion.datos["Personas"]:
            if "id" not in persona:
                persona["id"] = informacion.datos["Configuraciones"][0]["contador_id_bbdd"]

        with open(informacion.fichero, "w") as abrir:
            json.dump(informacion.datos, abrir, indent=4)
              
    def leer_persona(atr=None, valor=None): 
        resultados = {}
        for persona in informacion.datos["Personas"]:
            if (atr is None or valor is None) or (atr == "" and valor == ""):
                indice = informacion.datos["Personas"].index(persona)
                resultados[indice] = persona
        for persona in resultados.items():
            print(f'Datos: {persona}')

    def modificar_persona(id, atr, datos_persona):
        for persona in informacion.datos["Personas"]:
            if persona["id"] == id:
                print("Antes de Modificarlo:", persona)
                persona[atr] = datos_persona
                print("Despues de modificarlo:", persona)
    
        with open(informacion.fichero, "w") as modificar:
            json.dump(informacion.datos, modificar, indent=4)

    def borrar_persona(id): #Creamos el metodo para borrar una persona
        for persona in informacion.datos["Personas"]:
            if persona["id"] == id:
                print("Se eliminara:", persona)
                informacion.datos["Personas"].remove(persona)
        with open(informacion.fichero, "w") as modificar:
            json.dump(informacion.datos, modificar, indent=4)
