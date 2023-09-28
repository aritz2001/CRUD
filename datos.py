import os   
import json

class datos2():
    archivo = os.path.dirname(os.path.abspath(__file__))
    fichero = os.path.join(archivo + '/bbdd/' 'base_datos.json')
    def __init__(self):
        self.datos = self.leer_json()
    def leer_json(self):
        with open(self.fichero,"r") as leer:
            self.datos = json.load(leer)
            leer.close()
            
    