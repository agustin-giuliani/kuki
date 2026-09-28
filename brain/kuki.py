# -*- coding: utf-8 -*-

import json

# Genera las respuestas finales que verá el usuario.
from brain.response import ResponseGenerator

# Sistema principal de conocimiento.
from brain.learning.knowledge import Knowledge

# Sistema que decide cómo aprender y recordar.
from brain.learning.learner import Learning

# Integrador que incorpora conocimiento validado.
from brain.learning.knowledge_integrator import KnowledgeIntegrator

# Sistema de conocimiento pendiente de validación.
from brain.learning.pending_knowledge import PendingKnowledge

# Sistema principal de memoria.
from brain.learning.memory import Memory

# Integrador que estructura y administra la memoria.
from brain.learning.memory_integrator import MemoryIntegrator

# Procesador de lenguaje natural de KUKI.
from brain.language.processor import LanguageProcessor

# Historial de conversación.
from brain.conversation import Conversation

# Sistema que mantiene el tema/contexto actual.
from brain.context import ContextManager

# Administrador de herramientas.
from brain.tools.manager import ToolManager

# Planificador que decide cuándo utilizar una herramienta.
from brain.tools.planner import ToolPlanner

# Neurona simple utilizada actualmente por KUKI.
from brain.neuron import Neuron


class Kuki:

    def __init__(self):

        # --------------------------------------------------
        # MODELO / NEURONA
        # --------------------------------------------------

        # Creamos la neurona principal de KUKI.
        self.neurona = Neuron()

        # --------------------------------------------------
        # MEMORIA
        # --------------------------------------------------

        # Creamos el almacenamiento principal de memoria.
        self.memoria = Memory()

        # El MemoryIntegrator se encarga de integrar los datos
        # antes de guardarlos en la memoria.
        self.memory_integrator = MemoryIntegrator(
            self.memoria
        )

        # --------------------------------------------------
        # CONOCIMIENTO
        # --------------------------------------------------

        # Creamos el almacenamiento principal de conocimiento.
        self.conocimiento = Knowledge()

        # PendingKnowledge guarda información externa que todavía
        # no fue incorporada definitivamente al conocimiento.
        self.pending_knowledge = PendingKnowledge()

        # KnowledgeIntegrator se encarga de integrar conocimiento
        # que ya fue evaluado/validado.
        self.knowledge_integrator = KnowledgeIntegrator(
            self.conocimiento
        )

        # --------------------------------------------------
        # SISTEMA DE APRENDIZAJE
        # --------------------------------------------------

        # Learning funciona como coordinador del aprendizaje.
        #
        # Recibe memoria, conocimiento, conocimiento pendiente
        # y los dos integradores.
        self.aprendizaje = Learning(
            self.memoria,
            self.conocimiento,
            self.pending_knowledge,
            self.knowledge_integrator,
            self.memory_integrator
        )

        # --------------------------------------------------
        # LENGUAJE
        # --------------------------------------------------

        # Procesador que transforma el texto del usuario
        # en una intención estructurada.
        self.lenguaje = LanguageProcessor()

        # --------------------------------------------------
        # RESPUESTAS
        # --------------------------------------------------

        # Generador de respuestas finales.
        self.respuestas = ResponseGenerator()

        # --------------------------------------------------
        # CONVERSACIÓN Y CONTEXTO
        # --------------------------------------------------

        # Historial completo de la conversación.
        self.conversacion = Conversation()

        # Administrador del tema/contexto actual.
        self.contexto = ContextManager(
            self.conversacion
        )

        # --------------------------------------------------
        # HERRAMIENTAS
        # --------------------------------------------------

        # Administrador de herramientas disponibles.
        self.tools = ToolManager()

        # El planificador decide qué herramienta utilizar
        # cuando una intención necesita una herramienta.
        self.planificador = ToolPlanner(
            self.tools.catalogo,
            self.tools.selector
        )

        # --------------------------------------------------
        # CARGAR MODELO
        # --------------------------------------------------

        # Cargamos los parámetros de la neurona.
        self.cargar_modelo()

    def cargar_modelo(self):

        # Abrimos el archivo donde están guardados
        # los parámetros actuales de la neurona.
        with open(
            "models/kuki_neuron.json",
            "r",
            encoding="utf-8"
        ) as archivo:

            modelo = json.load(archivo)

        # Restauramos el peso aprendido.
        self.neurona.peso = modelo["peso"]

        # Restauramos el bias aprendido.
        self.neurona.bias = modelo["bias"]

        print("Modelo de KUKI cargado.")
        print("Peso:", self.neurona.peso)
        print("Bias:", self.neurona.bias)

    def pensar(self, entrada):

        # Ejecuta la predicción de la neurona.
        return self.neurona.predecir(
            entrada
        )

    def entender(self, texto):

        # Procesa el lenguaje del usuario y devuelve
        # una intención estructurada.
        return self.lenguaje.procesar(
            texto
        )

    def aprender(self, clave, valor):

        # Este método mantiene una interfaz simple de aprendizaje.
        #
        # Por ahora se conserva para compatibilidad con código
        # anterior. El flujo principal utiliza Learning.
        self.memoria.guardar(
            clave,
            valor
        )

    def recordar(self, clave):

        # Recupera directamente un dato de memoria.
        #
        # El flujo conversacional normalmente utiliza
        # Learning.recordar_memoria().
        return self.memoria.recordar(
            clave
        )

    def obtener_contexto(self, cantidad=10):

        # Devuelve los últimos mensajes de la conversación.
        return self.conversacion.obtener_recientes(
            cantidad
        )

    def responder(self, entrada):

        # --------------------------------------------------
        # 1. GUARDAR MENSAJE DEL USUARIO
        # --------------------------------------------------

        # Primero guardamos lo que dijo el usuario.
        self.conversacion.guardar(
            "usuario",
            entrada
        )

        # --------------------------------------------------
        # 2. ENTENDER EL MENSAJE
        # --------------------------------------------------

        # El LanguageProcessor transforma el texto
        # en una intención estructurada.
        resultado = self.lenguaje.procesar(
            entrada
        )

        # Obtenemos la intención detectada.
        intencion = resultado["intencion"]

        # --------------------------------------------------
        # 3. ACTUALIZAR CONTEXTO
        # --------------------------------------------------

        # El ContextManager analiza si el mensaje modifica
        # el tema actual de la conversación.
        tema_contextual = self.contexto.procesar(
            resultado
        )

        # --------------------------------------------------
        # 4. CREAR PLAN
        # --------------------------------------------------

        # El ToolPlanner determina si la intención necesita
        # utilizar alguna herramienta.
        plan = self.planificador.planificar(
            entrada,
            resultado
        )

        # Diccionario donde iremos acumulando información
        # necesaria para generar la respuesta.
        datos = {}

        # Todavía no tenemos una respuesta final.
        respuesta = None

        # --------------------------------------------------
        # 5. APRENDIZAJE
        # --------------------------------------------------

        # Learning decide si el mensaje representa
        # aprendizaje de memoria o de conocimiento.
        resultado_aprendizaje = self.aprendizaje.aprender(
            resultado
        )

        # Si Learning integró una memoria nueva o actualizó
        # una memoria existente, generamos una respuesta.
        if resultado_aprendizaje in (
            "memoria_integrada",
            "memoria_ya_existente"
        ):

            respuesta = "Lo recordare."

        # Si Learning incorporó conocimiento nuevo,
        # o detectó que ya existía, generamos una respuesta.
        elif resultado_aprendizaje in (
            "conocimiento",
            "conocimiento_igual",
            "conocimiento_nuevo_dato"
        ):

            respuesta = "Lo aprendere."

        # --------------------------------
        # VALIDAR CONOCIMIENTO
        # --------------------------------

        elif intencion == "validar_conocimiento":

            # Obtenemos la clave del conocimiento que
            # el usuario quiere validar.
            clave = resultado.get(
                "clave"
            )

            # Buscamos las afirmaciones pendientes
            # relacionadas con esa clave.
            pendientes = self.pending_knowledge.obtener(
                clave
            )

            # Si no hay conocimiento pendiente,
            # informamos esa situación al generador
            # de respuestas.
            if not pendientes:

                datos["clave"] = clave
                datos["conocimiento_pendiente"] = False

            else:

                # Por ahora tomamos la primera afirmación
                # pendiente encontrada para esa clave.
                #
                # Más adelante podremos permitir que KUKI
                # gestione varias afirmaciones y fuentes.
                pendiente = pendientes[0]

                # Extraemos el contenido que vamos a validar.
                valor = pendiente.get(
                    "valor"
                )

                # Le pedimos a Learning que integre
                # el conocimiento y retire la afirmación
                # de PendingKnowledge.
                resultado_validacion = (
                    self.aprendizaje.validar_conocimiento(
                        clave,
                        valor
                    )
                )

                # Guardamos los datos necesarios para
                # ResponseGenerator.
                datos["clave"] = clave
                datos["valor"] = valor
                datos["resultado_validacion"] = (
                    resultado_validacion
                )
                datos["conocimiento_pendiente"] = True

            # Generamos la respuesta final de KUKI.
            respuesta = self.respuestas.generar(
                intencion,
                datos
            )

        # --------------------------------------------------
        # 6. HERRAMIENTAS
        # --------------------------------------------------

        elif plan.get("necesita_herramienta"):

            # Obtenemos los datos que preparó el planificador.
            datos_plan = plan.get(
                "datos",
                {}
            )

            # Incorporamos esos datos a los datos
            # que utilizaremos para generar la respuesta.
            datos.update(
                datos_plan
            )

            # Ejecutamos el plan de herramienta.
            resultado_tool = self.tools.ejecutar_plan(
                plan
            )

            # Guardamos el resultado de la herramienta.
            datos["resultado_tool"] = resultado_tool

            # --------------------------------------------------
            # APRENDIZAJE DESDE INTERNET
            # --------------------------------------------------

            # Si la intención era aprender desde Internet
            # y la herramienta funcionó correctamente,
            # enviamos el resultado al sistema de aprendizaje.
            if (
                intencion == "aprender_internet"
                and resultado_tool.get("estado") == "ok"
            ):

                self.aprendizaje.aprender_externo(
                    resultado_tool
                )

            # Obtenemos el nombre de la herramienta utilizada.
            herramienta = plan.get(
                "herramienta"
            )

            # Guardamos el nombre para que ResponseGenerator
            # pueda construir la respuesta correspondiente.
            datos["herramienta"] = herramienta

            # Si la herramienta requiere permiso y no está autorizada,
            # solicitamos autorización al usuario.
            if resultado_tool["estado"] == "permiso_denegado":

                datos["permiso_denegado"] = True

                solicitud = self.tools.solicitar_permiso(
                    herramienta
                )

                datos["solicitud"] = solicitud

            # Generamos la respuesta correspondiente
            # a la herramienta utilizada.
            respuesta = self.respuestas.generar(
                intencion,
                datos
            )

        # --------------------------------------------------
        # 7. AUTORIZAR / RECHAZAR / REVOCAR HERRAMIENTA
        # --------------------------------------------------

        elif intencion in (
            "autorizar_herramienta",
            "rechazar_herramienta",
            "revocar_herramienta"
        ):

            # Ejecutamos la operación relacionada
            # con los permisos.
            resultado_autorizacion = self.tools.ejecutar_autorizacion(
                resultado
            )

            # Obtenemos el plan de autorización.
            plan_autorizacion = resultado_autorizacion["plan"]

            # Obtenemos el resultado de la operación.
            resultado = resultado_autorizacion["resultado"]

            # Guardamos qué herramienta estaba involucrada.
            datos["herramienta"] = plan_autorizacion.get(
                "herramienta"
            )

            # Guardamos el resultado de la autorización.
            datos["resultado_autorizacion"] = resultado

            # Si no se encontró una herramienta válida,
            # marcamos esta situación.
            if datos["herramienta"] is None:

                datos["herramienta_no_encontrada"] = True

            # Generamos la respuesta.
            respuesta = self.respuestas.generar(
                intencion,
                datos
            )

        # --------------------------------------------------
        # 8. CONSULTAR PERMISOS
        # --------------------------------------------------

        elif intencion == "consultar_permisos":

            # Obtenemos las herramientas disponibles
            # y su estado de autorización.
            datos["herramientas"] = self.tools.obtener_herramientas()

            # Generamos la respuesta.
            respuesta = self.respuestas.generar(
                intencion,
                datos
            )

        # --------------------------------------------------
        # 9. OTRAS INTENCIONES
        # --------------------------------------------------

        else:

            # --------------------------------------------------
            # IDENTIDAD DEL USUARIO
            # --------------------------------------------------

            if intencion == "identidad_usuario":

                # Recuperamos el nombre desde Memory a través
                # del sistema de aprendizaje.
                datos["nombre"] = self.aprendizaje.recordar_memoria(
                    "nombre"
                )

            # --------------------------------------------------
            # RECORDAR UNA MEMORIA
            # --------------------------------------------------

            elif intencion == "recordar":

                # Obtenemos la clave que detectó
                # LanguageProcessor.
                clave = resultado["clave"]

                # Guardamos la clave para ResponseGenerator.
                datos["clave"] = clave

                # Buscamos el valor en Memory.
                datos["valor"] = self.aprendizaje.recordar_memoria(
                    clave
                )

            # --------------------------------------------------
            # CONSULTAR CONOCIMIENTO
            # --------------------------------------------------

            elif intencion == "conocimiento":

                # Obtenemos el concepto que quiere consultar
                # el usuario.
                clave = resultado["clave"]

                # Obtenemos la categoría solicitada.
                categoria = resultado.get(
                    "categoria",
                    "descripcion"
                )

                # Guardamos ambos datos para la respuesta.
                datos["clave"] = clave
                datos["categoria"] = categoria

                # Buscamos el conocimiento correspondiente.
                datos["valor"] = self.aprendizaje.recordar_conocimiento(
                    clave,
                    categoria
                )

            # --------------------------------------------------
            # PREGUNTA CONTEXTUAL
            # --------------------------------------------------

            elif intencion == "pregunta_contextual":

                # Obtenemos el tema actual.
                tema = tema_contextual

                # Guardamos el tema para ResponseGenerator.
                datos["tema"] = tema

                # Actualmente las preguntas contextuales
                # buscan la categoría "usos".
                datos["categoria"] = "usos"

                # Si existe un tema actual, buscamos
                # información relacionada.
                if tema is not None:

                    datos["valor"] = self.aprendizaje.recordar_conocimiento(
                        tema,
                        "usos"
                    )

            # Generamos la respuesta final.
            respuesta = self.respuestas.generar(
                intencion,
                datos
            )

        # --------------------------------------------------
        # 10. GUARDAR RESPUESTA DE KUKI
        # --------------------------------------------------

        # Guardamos la respuesta final en el historial.
        self.conversacion.guardar(
            "kuki",
            respuesta
        )

        # Devolvemos la respuesta al usuario.
        return respuesta