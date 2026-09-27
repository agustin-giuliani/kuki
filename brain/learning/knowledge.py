import json
import os
from datetime import datetime


class Knowledge:

    def __init__(self, archivo="data/knowledge.json"):
        self.archivo = archivo

        carpeta = os.path.dirname(self.archivo)

        if carpeta:
            os.makedirs(carpeta, exist_ok=True)

        if not os.path.exists(self.archivo):
            with open(self.archivo, "w", encoding="utf-8") as archivo:
                json.dump({}, archivo, indent=4, ensure_ascii=False)

    def _normalizar_clave(self, clave):

        if not clave:
            return None

        return clave.strip().lower()

    def guardar(self, clave, valor, categoria="descripcion"):

        clave = self._normalizar_clave(
            clave
        )

        if not clave or not valor:
            return

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

    def existe(self, clave):

        clave = self._normalizar_clave(
            clave
        )

        if not clave:
            return False

        with open(
            self.archivo,
            "r",
            encoding="utf-8"
        ) as archivo:

            conocimiento = json.load(archivo)

        return clave in conocimiento


    def agregar_fuente(
        self,
        clave,
        tipo,
        url=None
    ):

        clave = self._normalizar_clave(
            clave
        )

        if not clave or not tipo:
            return False

        with open(self.archivo, "r", encoding="utf-8") as archivo:
            conocimiento = json.load(archivo)

        if clave not in conocimiento:
            return False

        if isinstance(conocimiento[clave], str):

            conocimiento[clave] = {
                "descripcion": conocimiento[clave]
            }

        if "fuentes" not in conocimiento[clave]:

            conocimiento[clave]["fuentes"] = []

        # --------------------------------
        # CREAR FUENTE
        # --------------------------------

        fuente = {
            "tipo": tipo,
            "fecha": datetime.now().strftime(
                "%Y-%m-%d"
            )
        }

        if url:
            fuente["url"] = url

        # --------------------------------
        # COMPROBAR FUENTE DUPLICADA
        # --------------------------------

        for fuente_existente in conocimiento[clave]["fuentes"]:

            if tipo == "internet":

                if (
                    fuente_existente.get("tipo") == "internet"
                    and fuente_existente.get("url") == url
                ):

                    return False

            elif tipo == "usuario":

                if fuente_existente.get("tipo") == "usuario":

                    return False

            else:

                if fuente_existente == fuente:

                    return False

        # --------------------------------
        # AGREGAR FUENTE
        # --------------------------------

        conocimiento[clave]["fuentes"].append(
            fuente
        )

        with open(self.archivo, "w", encoding="utf-8") as archivo:
            json.dump(
                conocimiento,
                archivo,
                indent=4,
                ensure_ascii=False
            )

        return True

    def recordar(self, clave, categoria="descripcion"):

        clave = self._normalizar_clave(
            clave
        )

        if not clave:
            return None

        with open(self.archivo, "r", encoding="utf-8") as archivo:
            conocimiento = json.load(archivo)

        if clave not in conocimiento:
            return None

        dato = conocimiento[clave]

        # Compatibilidad con el formato viejo
        if isinstance(dato, str):
            return dato

        return dato.get(categoria)

    def obtener(self, clave):

        clave = self._normalizar_clave(
            clave
        )

        if not clave:
            return None

        with open(
            self.archivo,
            "r",
            encoding="utf-8"
        ) as archivo:

            conocimiento = json.load(
                archivo
            )

        if clave not in conocimiento:
            return None

        dato = conocimiento[clave]

        if isinstance(dato, str):
            return {
                "descripcion": dato
            }

        return dato