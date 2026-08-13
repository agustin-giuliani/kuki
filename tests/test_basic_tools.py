from brain.tools.registry import ToolRegistry
from brain.tools.permissions import PermissionManager
from brain.tools.executor import ToolExecutor

from brain.tools.basic import obtener_hora


registry = ToolRegistry()
permissions = PermissionManager()

registry.registrar(
    "hora",
    obtener_hora,
    "Obtiene la hora actual."
)

permissions.registrar(
    "hora",
    True
)

executor = ToolExecutor(
    registry,
    permissions
)


print("--- TOOL HORA ---")

resultado = executor.ejecutar("hora")

print(resultado)
