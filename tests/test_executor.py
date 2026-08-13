from brain.tools.registry import ToolRegistry
from brain.tools.permissions import PermissionManager
from brain.tools.executor import ToolExecutor


def saludar(nombre):

    return "Hola " + nombre


registry = ToolRegistry()
permissions = PermissionManager()

registry.registrar(
    "saludar",
    saludar,
    "Saluda a una persona."
)

permissions.registrar(
    "saludar",
    "seguro",
    False
)

executor = ToolExecutor(
    registry,
    permissions
)


print("--- TOOL EXECUTOR ---")

print()
print("Intento sin permiso:")

resultado = executor.ejecutar(
    "saludar",
    "Agustin"
)

print(resultado)


print()
print("Concediendo permiso...")

permissions.conceder("saludar")

resultado = executor.ejecutar(
    "saludar",
    "Agustin"
)

print(resultado)
