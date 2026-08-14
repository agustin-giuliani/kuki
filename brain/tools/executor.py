from brain.tools.result import ToolResult


class ToolExecutor:

    def __init__(self, registry, permissions):

        self.registry = registry
        self.permissions = permissions

    def ejecutar(self, nombre, *args, **kwargs):

        if not self.registry.existe(nombre):

            return ToolResult(
                "error",
                mensaje="La herramienta no existe.",
                herramienta=nombre
            ).to_dict()

        if not self.permissions.tiene_permiso(nombre):

            return ToolResult(
                "permiso_denegado",
                mensaje=(
                    "KUKI no tiene permiso para "
                    "usar esta herramienta."
                ),
                herramienta=nombre
            ).to_dict()

        herramienta = self.registry.obtener(
            nombre
        )

        funcion = herramienta["funcion"]

        try:

            resultado = funcion(
                *args,
                **kwargs
            )

            return ToolResult(
                "ok",
                resultado=resultado,
                herramienta=nombre
            ).to_dict()

        except Exception as error:

            return ToolResult(
                "error",
                mensaje=str(error),
                herramienta=nombre
            ).to_dict()
