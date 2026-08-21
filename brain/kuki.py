# -*- coding: utf-8 -*-

import json

from brain.response import ResponseGenerator
from brain.learning.knowledge import Knowledge
from brain.learning.learner import Learning
from brain.neuron import Neuron
from brain.learning.memory import Memory
from brain.language.processor import LanguageProcessor
from brain.conversation import Conversation
from brain.context import ContextManager
from brain.tools.manager import ToolManager
from brain.tools.planner import ToolPlanner



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

        self.planificador = ToolPlanner(
            self.tools.catalogo,
            self.tools.selector
        )

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
        self.conversacion.guardar(
            "usuario",
            entrada
        )

        # 1. Entender
        resultado = self.lenguaje.procesar(
            entrada
        )

        intencion = resultado["intencion"]

        tema_contextual = self.contexto.procesar(
            resultado
        )

        # 2. Crear plan
        plan = self.planificador.planificar(
            entrada,
            resultado
        )

        datos = {}

        respuesta = None

        # --------------------------------
        # APRENDIZAJE
        # --------------------------------

        tipo = self.aprendizaje.aprender(
            resultado
        )

        if tipo == "memoria":

            respuesta = "Lo recordare."

        elif tipo == "conocimiento":

            respuesta = "Lo aprendere."

        # --------------------------------
        # HERRAMIENTAS
        # --------------------------------

        elif plan.get("necesita_herramienta"):

            datos_plan = plan.get(
                "datos",
                {}
            )

            datos.update(
                datos_plan
            )

            resultado_tool = self.tools.ejecutar_plan(
                plan
            )

            datos["resultado_tool"] = resultado_tool

            herramienta = plan.get(
                "herramienta"
            )

            datos["herramienta"] = herramienta

            if resultado_tool["estado"] == "permiso_denegado":

                datos["permiso_denegado"] = True

                solicitud = self.tools.solicitar_permiso(
                    herramienta
                )

                datos["solicitud"] = solicitud

            respuesta = self.respuestas.generar(
                intencion,
                datos
            )

        # --------------------------------
        # AUTORIZAR/rechazar HERRAMIENTA
        # --------------------------------

        elif intencion in (
            "autorizar_herramienta",
            "rechazar_herramienta",
            "revocar_herramienta"
        ):

            resultado_autorizacion = self.tools.ejecutar_autorizacion(
                resultado
            )

            plan_autorizacion = resultado_autorizacion["plan"]

            resultado = resultado_autorizacion["resultado"]

            datos["herramienta"] = plan_autorizacion.get(
                "herramienta"
            )

            datos["resultado_autorizacion"] = resultado

            if datos["herramienta"] is None:

                datos["herramienta_no_encontrada"] = True

            respuesta = self.respuestas.generar(
                intencion,
                datos
            )
        
        elif intencion == "consultar_permisos":

            datos["herramientas"] = self.tools.obtener_herramientas()

            respuesta = self.respuestas.generar(
                intencion,
                datos
            )

        # --------------------------------
        # OTRAS INTENCIONES
        # --------------------------------

        else:
            if intencion == "identidad_usuario":

                datos["nombre"] = self.aprendizaje.recordar_memoria(
                    "nombre"
                )

            elif intencion == "recordar":

                clave = resultado["clave"]

                datos["clave"] = clave
                datos["valor"] = self.aprendizaje.recordar_memoria(
                    clave
            )

            elif intencion == "conocimiento":

                clave = resultado["clave"]

                categoria = resultado.get(
                    "categoria",
                    "descripcion"
                )

                datos["clave"] = clave
                datos["categoria"] = categoria

                datos["valor"] = self.aprendizaje.recordar_conocimiento(
                    clave,
                    categoria
                )

            elif intencion == "pregunta_contextual":

                tema = tema_contextual

                datos["tema"] = tema
                datos["categoria"] = "usos"

                if tema is not None:

                    datos["valor"] = self.aprendizaje.recordar_conocimiento(
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
