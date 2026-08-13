import json
import os


class Knowledge:

    def __init__(self, archivo="data/knowledge.json"):
        self.archivo = archivo

        carpeta = os.path.dirname(self.archivo)

        if carpeta:
            os.makedirs(carpeta, exist_ok=True)

        if not os.path.exists(self.archivo):
            with open(self.archivo, "w", encoding="utf-8") as archivo:
                json.dump({}, archivo, indent=4, ensure_ascii=False)

    def guardar(self, clave, valor, categoria="descripcion"):

        with open(self.archivo, "r", encoding="utf-8") as archivo:
            conocimiento = json.load(archivo)

        if clave not in conocimiento:

            conocimiento[clave] = {
                categoria: valor
            }

        elif isinstance(conocimiento[clave], str):

            valor_anterior = conocimiento[clave]

            conocimiento[clave] = {
                "descripcion": valor_anterior,
                categoria: valor
            }

        else:

            conocimiento[clave][categoria] = valor

        with open(self.archivo, "w", encoding="utf-8") as archivo:
            json.dump(
                conocimiento,
                archivo,
                indent=4,
                ensure_ascii=False
            )

    def recordar(self, clave, categoria="descripcion"):

        with open(self.archivo, "r", encoding="utf-8") as archivo:
            conocimiento = json.load(archivo)

        if clave not in conocimiento:
            return None

        dato = conocimiento[clave]

        # Compatibilidad con el formato viejo
        if isinstance(dato, str):
            return dato

        return dato.get(categoria)