from brain.tools.manager import ToolManager


tools = ToolManager()


print("--- CATALOGO DE KUKI ---")

print()
print("Informacion de la herramienta hora:")

info = tools.obtener_info("hora")

print(info)

print()
print("Todas las herramientas:")

herramientas = tools.listar_detallado()

for herramienta in herramientas:

    print(
        "Nombre:",
        herramienta["nombre"]
    )

    print(
        "Descripcion:",
        herramienta["descripcion"]
    )

    print(
        "Nivel:",
        herramienta["nivel"]
    )

    print(
        "Permitido:",
        herramienta["permitido"]
    )

    print()
