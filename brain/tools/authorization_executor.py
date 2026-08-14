class AuthorizationExecutor:

    def __init__(self, authorization_manager):

        self.authorization_manager = authorization_manager

    def ejecutar(self, plan, origen="usuario"):

        if not plan.get("necesita_autorizacion"):

            return {
                "estado": "sin_autorizacion",
                "herramienta": None
            }

        herramienta = plan.get(
            "herramienta"
        )

        accion = plan.get(
            "accion"
        )

        if herramienta is None:

            return {
                "estado": "error",
                "mensaje": "No se especifico una herramienta.",
                "herramienta": None
            }

        if accion == "aprobar":

            return self.authorization_manager.aprobar(
                herramienta,
                origen=origen
            )

        if accion == "rechazar":

            return self.authorization_manager.rechazar(
                herramienta,
                origen=origen
            )

        return {
            "estado": "accion_no_valida",
            "mensaje": "La accion de autorizacion no es valida.",
            "herramienta": herramienta
        }
