class ToolExecutor:

    def __init__(self, registry, permissions):
        self.registry = registry
        self.permissions = permissions

    def ejecutar(self, nombre, *args, **kwargs):

        # La herramienta debe existir
        if not self.registry.existe(nombre):
            return {
                "estado": "error",
                "mensaje": "La herramienta no existe."
            }

        # La herramienta debe tener permiso
        if not self.permissions.tiene_permiso(nombre):
            return {
                "estado": "permiso_denegado",
                "mensaje": "KUKI no tiene permiso para usar esta herramienta."
            }

        herramienta = self.registry.obtener(nombre)

        funcion = herramienta["funcion"]

        try:

            resultado = funcion(*args, **kwargs)

            return {
                "estado": "ok",
                "resultado": resultado
            }

        except Exception as error:

            return {
                "estado": "error",
                "mensaje": str(error)
            }
