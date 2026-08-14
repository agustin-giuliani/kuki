class AuthorizationPlanner:

    def __init__(self, selector):

        self.selector = selector

    def planificar(self, resultado_lenguaje):

        intencion = resultado_lenguaje.get(
            "intencion"
        )

        texto = resultado_lenguaje.get(
            "texto",
            ""
        )

        if intencion == "autorizar_herramienta":

            herramienta = self.selector.seleccionar(
                texto
            )

            return {
                "necesita_autorizacion": True,
                "accion": "aprobar",
                "herramienta": herramienta,
                "datos": {}
            }

        if intencion == "rechazar_herramienta":

            herramienta = self.selector.seleccionar(
                texto
            )

            return {
                "necesita_autorizacion": True,
                "accion": "rechazar",
                "herramienta": herramienta,
                "datos": {}
            }

        return {
            "necesita_autorizacion": False,
            "accion": None,
            "herramienta": None,
            "datos": {}
        }
