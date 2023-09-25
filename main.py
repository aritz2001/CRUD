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

    def crear_persona(self): #Creamos el metodo para crear una persona
        with open(fichero,"w") as abrir:
            datos["Configuraciones"][0]["contador_id_bbdd"]
            json.dump(datos, abrir, indent=4)
            abrir.close()
        #datos= last.id + 1
            print("El contador esta ahora en: ", datos["Configuraciones"][0]["contador_id_bbdd"])            
            Persona.identificador += 1 #Incrementamos el identificador

            nueva_persona = Persona(
                self.nombre, 
                self.apellido, 
                self.edad, 
                self.telefono, 
                self.direccion, 
                self.email
            ).__dict__
        with open(fichero,"w") as modificar:
            datos['Personas'].append(nueva_persona)
            json.dump(datos, modificar, indent=4)
            modificar.close()
       # modificar_json()

    def leer_persona(atr,valor): #Creamos el metodo para leer una persona
        resultados = {}
        for persona in datos["Personas"]:
            if persona[atr] == valor or valor == "all":
                indice = datos["Personas"].index(persona)
                resultados[indice] = persona
    
        return (resultados)

    def modificar_persona(id,atr,datos_persona): #Creamos el metodo para modificar una persona
        for persona in datos["Personas"]:
            if persona["id"] == id:
                print(persona)
                indice = datos["Personas"].index(persona)
                datos["Personas"][indice][atr] = datos_persona
                print(datos["Personas"][indice][atr])
         #       modificar_json()

    def borrar_persona(id): #Creamos el metodo para borrar una persona
        for persona in datos["Personas"]:
            if persona["id"] == id:
                print("Se eliminara:", persona)
                indice = datos["Personas"].index(persona)
                datos["Personas"].pop(indice)
         #       modificar_json()


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
        
        Persona().leer_persona()
    elif variable == 3:
        id = int(input("Ingrese el id a modificar: "))
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        edad = int(input("Ingrese su edad: "))
        telefono = int(input("Ingrese su telefono: "))
        direccion = input("Ingrese su direccion: ")
        email = input("Ingrese su email: ") 
        datos_persona = [nombre, apellido, edad,telefono,direccion,email]
        Persona(id,nombre, apellido, edad,telefono,direccion,email).modificar_persona(datos_persona)
    elif variable == 4:
        id = int(input("Ingrese el id a borrar: "))
        Persona(id).borrar_persona()
    elif variable >= 5 or variable == 0:
        print("Ha salido del programa")
        break