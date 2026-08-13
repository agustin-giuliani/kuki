import json
import os
from datetime import datetime


class Conversation:

    def __init__(self, archivo="data/conversation.json"):
        self.archivo = archivo

        carpeta = os.path.dirname(self.archivo)

        if carpeta:
            os.makedirs(carpeta, exist_ok=True)

        if not os.path.exists(self.archivo):
            with open(self.archivo, "w", encoding="utf-8") as archivo:
                json.dump([], archivo, indent=4)

    def guardar(self, rol, mensaje):

        with open(self.archivo, "r", encoding="utf-8") as archivo:
            conversaciones = json.load(archivo)

        conversaciones.append({
            "rol": rol,
            "mensaje": mensaje,
            "fecha": datetime.now().isoformat()
        })

        with open(self.archivo, "w", encoding="utf-8") as archivo:
            json.dump(
                conversaciones,
                archivo,
                indent=4,
                ensure_ascii=False
            )

    def obtener_historial(self):

        with open(self.archivo, "r", encoding="utf-8") as archivo:
            return json.load(archivo)

    def obtener_recientes(self, cantidad=10):

        historial = self.obtener_historial()

        return historial[-cantidad:]

    def obtener_ultimo_usuario(self):

        historial = self.obtener_historial()

        for mensaje in reversed(historial):

            if mensaje["rol"] == "usuario":
                return mensaje["mensaje"]

        return None
