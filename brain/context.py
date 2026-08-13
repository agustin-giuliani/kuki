class ContextManager:

    def __init__(self, conversacion):
        self.conversacion = conversacion
        self.tema_actual = None

    def obtener_contexto(self, cantidad=10):

        mensajes = self.conversacion.obtener_recientes(cantidad)

        return {
            "mensajes": mensajes,
            "tema": self.tema_actual
        }

    def establecer_tema(self, tema):

        self.tema_actual = tema

    def obtener_tema(self):

        return self.tema_actual

    def actualizar_tema(self, resultado):

        if resultado["intencion"] == "conocimiento":

            clave = resultado.get("clave")

            if clave:
                self.tema_actual = clave

        return self.tema_actual