class PermissionManager:

    NIVELES = {
        "seguro": 0,
        "autorizacion": 1,
        "alto": 2,
        "critico": 3
    }

    def __init__(self):
        self.permisos = {}

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

    def conceder(self, herramienta):

        if herramienta not in self.permisos:
            return False

        self.permisos[herramienta]["permitido"] = True

        return True

    def revocar(self, herramienta):

        if herramienta not in self.permisos:
            return False

        self.permisos[herramienta]["permitido"] = False

        return True

    def listar(self):

        return self.permisos.copy()
