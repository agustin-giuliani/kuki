# -*- coding: utf-8 -*-

import json

from brain.response import ResponseGenerator
from brain.knowledge import Knowledge
from brain.learning import Learning
from brain.neuron import Neuron
from brain.memory import Memory
from brain.language import LanguageProcessor
from brain.conversation import Conversation
from brain.context import ContextManager
from brain.tools.manager import ToolManager



class Kuki:

    def __init__(self):
        self.neurona = Neuron()
        self.memoria = Memory()
        self.conocimiento = Knowledge()
        self.aprendizaje = Learning(
                self.memoria,
                self.conocimiento
        )

        self.lenguaje = LanguageProcessor()
        self.respuestas = ResponseGenerator()
        self.conversacion = Conversation()
        self.contexto = ContextManager(self.conversacion)

        self.tools = ToolManager()

        self.cargar_modelo()

    def cargar_modelo(self):

        with open(
            "models/kuki_neuron.json",
            "r",
            encoding="utf-8"
        ) as archivo:

            modelo = json.load(archivo)

        self.neurona.peso = modelo["peso"]
        self.neurona.bias = modelo["bias"]

        print("Modelo de KUKI cargado.")
        print("Peso:", self.neurona.peso)
        print("Bias:", self.neurona.bias)

    def pensar(self, entrada):

        return self.neurona.predecir(entrada)

    def entender(self, texto):
        return self.lenguaje.procesar(texto)

    def aprender(self, clave, valor):

        self.memoria.guardar(clave, valor)

    def recordar(self, clave):

        return self.memoria.recordar(clave)

    def obtener_contexto(self, cantidad=10):

        return self.conversacion.obtener_recientes(cantidad)

    def responder(self, entrada):

        # Guardamos el mensaje del usuario
        self.conversacion.guardar("usuario", entrada)

        # 1. Entender primero
        resultado = self.lenguaje.procesar(entrada)

        intencion = resultado["intencion"]

        self.contexto.actualizar_tema(resultado)

        herramienta = self.tools.seleccionar(entrada)

        datos = {}

        respuesta = None

        # 2. Aprendizaje de memoria personal
        if intencion == "aprendizaje_memoria":

            tipo = self.aprendizaje.aprender_frase(entrada)

            if tipo == "memoria":
                respuesta = "Lo recordare."
            else:
                respuesta = "No pude aprender eso."

        # 3. Aprendizaje de conocimiento
        elif intencion == "aprendizaje_conocimiento":

            tipo = self.aprendizaje.aprender_frase(entrada)

            if tipo == "conocimiento":
                respuesta = "Lo aprendere."
            else:
                respuesta = "No pude aprender eso."

        elif intencion == "usar_herramienta":

            resultado_tool = self.tools.ejecutar_seleccion(
                entrada
            )

            datos["herramienta"] = resultado_tool.get(
                "herramienta"
            )

            datos["resultado_tool"] = resultado_tool

            if resultado_tool["estado"] == "herramienta_no_encontrada":

                datos["herramienta_no_encontrada"] = True

            elif resultado_tool["estado"] == "permiso_denegado":

                datos["permiso_denegado"] = True

            respuesta = self.respuestas.generar(
                intencion,
                datos
            )

        # 4. Preparar datos para la respuesta
        else:

            if intencion == "hora":

                if herramienta == "hora":

                    resultado_tool = self.tools.ejecutar(
                        herramienta
                    )

                    if resultado_tool["estado"] == "ok":

                        datos["hora"] = resultado_tool["resultado"]

                    else:

                        datos["permiso_denegado"] = True

                else:

                    datos["permiso_denegado"] = True

            elif intencion == "identidad_usuario":

                datos["nombre"] = self.memoria.recordar("nombre")

            elif intencion == "recordar":

                clave = resultado["clave"]

                datos["clave"] = clave
                datos["valor"] = self.memoria.recordar(clave)

            elif intencion == "conocimiento":

                clave = resultado["clave"]
                categoria = resultado.get("categoria", "descripcion")

                datos["clave"] = clave
                datos["categoria"] = categoria
                datos["valor"] = self.conocimiento.recordar(
                    clave,
                    categoria
                )

            elif intencion == "pregunta_contextual":

                tema = self.contexto.obtener_tema()

                datos["tema"] = tema
                datos["categoria"] = "usos"

                if tema is not None:
                    datos["valor"] = self.conocimiento.recordar(
                        tema,
                        "usos"
                    )

            respuesta = self.respuestas.generar(
                intencion,
                datos
            )

        # --------------------------------
        # GUARDAR RESPUESTA
        # --------------------------------

        self.conversacion.guardar(
            "kuki",
            respuesta
        )

        return respuesta
