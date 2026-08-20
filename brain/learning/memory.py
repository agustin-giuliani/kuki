import json
import os


class Memory:

    def __init__(self, archivo="data/memory.json"):
        self.archivo = archivo

        os.makedirs(os.path.dirname(self.archivo), exist_ok=True)

        if not os.path.exists(self.archivo):
            with open(self.archivo, "w", encoding="utf-8") as archivo:
                json.dump({}, archivo, indent=4)

    def guardar(self, clave, valor):

        with open(self.archivo, "r", encoding="utf-8") as archivo:
            memoria = json.load(archivo)

        memoria[clave] = valor

        with open(self.archivo, "w", encoding="utf-8") as archivo:
            json.dump(memoria, archivo, indent=4, ensure_ascii=False)

    def recordar(self, clave):

        with open(self.archivo, "r", encoding="utf-8") as archivo:
            memoria = json.load(archivo)

        return memoria.get(clave)
