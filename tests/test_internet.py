from brain.tools.manager import ToolManager


tools = ToolManager()


print("--- INTERNET TOOL ---")

print()
print("Sin permiso:")

resultado = tools.ejecutar(
    "internet",
    "https://example.com"
)

print(resultado)


print()
print("Concediendo permiso...")

tools.permissions.conceder(
    "internet",
    origen="usuario"
)

print(
    tools.ejecutar(
        "internet",
        "https://example.com"
    )
)
