class ToolPlanner:

    def __init__(self, catalogo, selector):
        self.catalogo = catalogo
        self.selector = selector

    def planificar(self, texto, resultado_lenguaje):

        intencion = resultado_lenguaje["intencion"]

        # --------------------------------
        # BUSCAR HERRAMIENTA POR CAPACIDAD
        # --------------------------------

        herramienta = self.catalogo.buscar_por_capacidad(
            intencion
        )

        if herramienta is not None:

            datos = {}

            if intencion == "buscar_internet":

                datos["consulta"] = resultado_lenguaje.get(
                    "consulta"
                )

            return {
                "necesita_herramienta": True,
                "herramienta": herramienta,
                "motivo": (
                    "Una herramienta puede resolver "
                    "esta intencion."
                ),
                "datos": datos
            }

        # --------------------------------
        # USO EXPLICITO DE HERRAMIENTA
        # --------------------------------

        if intencion == "usar_herramienta":

            herramienta = self.selector.seleccionar(
                texto
            )

            if herramienta is None:

                return {
                    "necesita_herramienta": False,
                    "herramienta": None,
                    "motivo": (
                        "No se encontro una herramienta adecuada."
                    ),
                    "datos": {}
                }

            return {
                "necesita_herramienta": True,
                "herramienta": herramienta,
                "motivo": (
                    "El usuario solicito utilizar "
                    "una herramienta."
                ),
                "datos": {}
            }

        # --------------------------------
        # SIN HERRAMIENTA
        # --------------------------------

        return {
            "necesita_herramienta": False,
            "herramienta": None,
            "motivo": "No se necesita una herramienta.",
            "datos": {}
        }