class ToolCatalog:

    def __init__(self, registry, permissions):

        self.registry = registry
        self.permissions = permissions

    def obtener(self, nombre):

        herramienta = self.registry.obtener(nombre)

        if herramienta is None:
            return None

        return {
            "nombre": nombre,
            "descripcion": herramienta["descripcion"],
            "nivel": self.permissions.nivel(nombre),
            "permitido": self.permissions.tiene_permiso(nombre)
        }

    def listar(self):

        herramientas = []

        for nombre in self.registry.listar():

            informacion = self.obtener(nombre)

            if informacion is not None:
                herramientas.append(informacion)

        return herramientas
