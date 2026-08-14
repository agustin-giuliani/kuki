from datetime import datetime

class PermissionManager:

    NIVELES = {
        "seguro": 0,
        "autorizacion": 1,
        "alto": 2,
        "critico": 3
    }

    def __init__(self):
        self.permisos = {}
        self.historial = []

    def registrar(
        self,
        herramienta,
        nivel="autorizacion",
        permitido=False
    ):

        if nivel not in self.NIVELES:
            raise ValueError(
                "Nivel de permiso no valido."
            )

        self.permisos[herramienta] = {
            "nivel": nivel,
            "permitido": permitido
        }

    def tiene_permiso(self, herramienta):

        permiso = self.permisos.get(herramienta)

        if permiso is None:
            return False

        return permiso["permitido"]

    def nivel(self, herramienta):

        permiso = self.permisos.get(herramienta)

        if permiso is None:
            return None

        return permiso["nivel"]

    def obtener_info(self, herramienta):

        permiso = self.permisos.get(herramienta)

        if permiso is None:
            return None

        return {
            "nombre": herramienta,
            "nivel": permiso["nivel"],
            "permitido": permiso["permitido"]
        }


    def conceder(self, herramienta, origen="usuario"):

        if herramienta not in self.permisos:
            return False

        self.permisos[herramienta]["permitido"] = True

        self.registrar_evento(
            herramienta,
            "conceder",
            origen
        )

        return True

    def revocar(self, herramienta, origen="usuario"):

        if herramienta not in self.permisos:
            return False

        self.permisos[herramienta]["permitido"] = False

        self.registrar_evento(
            herramienta,
            "revocar",
            origen
        )

        return True
    def listar(self):

        return self.permisos.copy()

    def registrar_evento(
        self,
        herramienta,
        accion,
        origen="usuario"
    ):

        evento = {
            "herramienta": herramienta,
            "accion": accion,
            "origen": origen,
            "fecha": datetime.now().isoformat()
        }

        self.historial.append(evento)

    def obtener_historial(self):

        return self.historial.copy()
