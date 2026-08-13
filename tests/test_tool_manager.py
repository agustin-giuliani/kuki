from brain.tools.manager import ToolManager


tools = ToolManager()


print("--- TOOL MANAGER ---")

print()
print("Herramientas:")
print(tools.listar())

print()
print("Ejecutando hora:")

resultado = tools.ejecutar("hora")

print(resultado)
