from brain.tools.manager import ToolManager


tools = ToolManager()


print("--- BUSQUEDA EN INTERNET ---")

print()
print("Sin permiso:")

resultado = tools.ejecutar(
    "internet",
    "Python"
)

print(resultado)


print()
print("Concediendo permiso...")

tools.permissions.conceder(
    "internet",
    origen="usuario"
)

resultado = tools.ejecutar(
    "internet",
    "Python"
)

print()
print("Resultado:")

print(resultado)
