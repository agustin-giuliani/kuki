# -*- coding: utf-8 -*-


class ContextManager:

    def __init__(self, conversacion):

        self.conversacion = conversacion
        self.tema_actual = None

    def obtener_contexto(self, cantidad=10):

        mensajes = self.conversacion.obtener_recientes(
            cantidad
        )

        return {
            "mensajes": mensajes,
            "tema": self.tema_actual
        }

    def establecer_tema(self, tema):

        if tema:

            self.tema_actual = tema.strip().lower()

        return self.tema_actual

    def obtener_tema(self):

        return self.tema_actual

    def actualizar_tema(self, resultado):

        if not resultado:
            return self.tema_actual

        intencion = resultado.get("intencion")

        if intencion == "conocimiento":

            clave = resultado.get("clave")

            if clave:
                self.establecer_tema(
                    clave
                )

        elif intencion in (
            "buscar_internet",
            "aprender_internet"
        ):

            consulta = resultado.get("consulta")

            if consulta:
                self.establecer_tema(
                    consulta
                )

        return self.tema_actual

    def es_pregunta_contextual(self, resultado):

        if not resultado:
            return False

        return resultado.get(
            "intencion"
        ) == "pregunta_contextual"

    def resolver_tema(self, resultado):

        if self.es_pregunta_contextual(resultado):

            return self.tema_actual

        return None

    def procesar(self, resultado):

        if not resultado:
            return self.tema_actual

        self.actualizar_tema(
            resultado
        )

        return self.obtener_tema()