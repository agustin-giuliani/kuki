class ToolPlanner:

    def __init__(self, selector):
        self.selector = selector

    def planificar(self, texto, resultado_lenguaje):

        intencion = resultado_lenguaje["intencion"]

        if intencion == "buscar_internet":
            return {
                "necesita_herramienta": True,
                "herramienta": "internet",
                "motivo": "Necesita informacion externa.",
                "datos": {
                    "consulta": resultado_lenguaje.get("consulta")
                }
            }

        if intencion == "hora":
            return {
                "necesita_herramienta": True,
                "herramienta": "hora",
                "motivo": "Necesita consultar la hora actual.",
                "datos": {}
            }

        if intencion == "usar_herramienta":

            herramienta = self.selector.seleccionar(texto)

            if herramienta is None:
                return {
                    "necesita_herramienta": False,
                    "herramienta": None,
                    "motivo": "No se encontro una herramienta adecuada.",
                    "datos": {}
                }

            return {
                "necesita_herramienta": True,
                "herramienta": herramienta,
                "motivo": "El usuario solicito utilizar una herramienta.",
                "datos": {}
            }

        return {
            "necesita_herramienta": False,
            "herramienta": None,
            "motivo": "No se necesita una herramienta.",
            "datos": {}
        }
