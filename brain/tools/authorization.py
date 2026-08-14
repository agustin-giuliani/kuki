class AuthorizationManager:

    def __init__(self, permissions):

        self.permissions = permissions
        self.solicitudes = []

    def solicitar(self, herramienta, origen="kuki"):

        if herramienta not in self.permissions.permisos:

            return {
                "estado": "herramienta_no_encontrada",
                "herramienta": herramienta
            }

        if self.permissions.tiene_permiso(herramienta):

            return {
                "estado": "ya_autorizado",
                "herramienta": herramienta
            }

        for solicitud in self.solicitudes:

            if (
                solicitud["herramienta"] == herramienta
                and solicitud["estado"] == "pendiente"
            ):

                return {
                    "estado": "ya_pendiente",
                    "herramienta": herramienta
                }

        solicitud = {
            "herramienta": herramienta,
            "origen": origen,
            "estado": "pendiente"
        }

        self.solicitudes.append(solicitud)

        return solicitud

    def listar_solicitudes(self):

        return self.solicitudes.copy()

    def aprobar(self, herramienta, origen="usuario"):

        if origen != "usuario":

            return {
                "estado": "permiso_denegado",
                "mensaje": (
                    "Solo el usuario puede aprobar permisos."
                ),
                "herramienta": herramienta
            }

        solicitud_encontrada = False

        for solicitud in self.solicitudes:

            if (
                solicitud["herramienta"] == herramienta
                and solicitud["estado"] == "pendiente"
            ):

                solicitud_encontrada = True
                break

        if not solicitud_encontrada:

            return {
                "estado": "sin_solicitud",
                "herramienta": herramienta
            }

        resultado = self.permissions.conceder(
            herramienta,
            origen="usuario"
        )

        if not resultado:

            return {
                "estado": "error",
                "herramienta": herramienta
            }

        for solicitud in self.solicitudes:

            if (
                solicitud["herramienta"] == herramienta
                and solicitud["estado"] == "pendiente"
            ):

                solicitud["estado"] = "aprobada"

        return {
            "estado": "aprobada",
            "herramienta": herramienta
        }

    def rechazar(self, herramienta, origen="usuario"):

        if origen != "usuario":

            return {
                "estado": "permiso_denegado",
                "mensaje": (
                    "Solo el usuario puede rechazar permisos."
                ),
                "herramienta": herramienta
            }

        solicitud_encontrada = False

        for solicitud in self.solicitudes:

            if (
                solicitud["herramienta"] == herramienta
                and solicitud["estado"] == "pendiente"
            ):

                solicitud["estado"] = "rechazada"
                solicitud_encontrada = True

        if not solicitud_encontrada:

            return {
                "estado": "sin_solicitud",
                "herramienta": herramienta
            }

        return {
            "estado": "rechazada",
            "herramienta": herramienta
        }