from brain.tools.registry import ToolRegistry
from brain.tools.permissions import PermissionManager
from brain.tools.executor import ToolExecutor
from brain.tools.basic import obtener_hora


class ToolManager:

    def __init__(self):

        self.registry = ToolRegistry()
        self.permissions = PermissionManager()

        self._registrar_herramientas()

        self.executor = ToolExecutor(
            self.registry,
            self.permissions
        )

    def _registrar_herramientas(self):

        self.registry.registrar(
            "hora",
            obtener_hora,
            "Obtiene la hora actual."
        )

        self.permissions.registrar(
            "hora",
            "seguro",
            True
        )

    def ejecutar(self, nombre, *args, **kwargs):

        return self.executor.ejecutar(
            nombre,
            *args,
            **kwargs
        )

    def listar(self):

        return self.registry.listar()
