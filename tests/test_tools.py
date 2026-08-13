from brain.tools.registry import ToolRegistry


def saludar():
    return "Hola desde una herramienta."


registry = ToolRegistry()

registry.registrar(
    "saludar",
    saludar,
    "Una herramienta que devuelve un saludo."
)

print("--- TOOLS DE KUKI ---")

print("Herramientas:", registry.listar())

print("Existe saludar:", registry.existe("saludar"))

herramienta = registry.obtener("saludar")

print("Descripcion:", herramienta["descripcion"])