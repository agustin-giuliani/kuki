from brain.tools.manager import ToolManager


tools = ToolManager()


print("--- TOOL MANAGER ---")

print()
print("Herramientas:")
print(tools.listar())

print()
print("Seleccion de herramienta:")

entradas = [
    "que hora es",
    "necesito saber la hora",
    "quiero consultar internet",
    "hola"
]

for entrada in entradas:

    herramienta = tools.seleccionar(
        entrada
    )

    print()
    print("Entrada:", entrada)
    print("Herramienta:", herramienta)


print()
print("Ejecutando hora:")

resultado = tools.ejecutar("hora")

print()
print("--- EJECUCION POR SELECCION ---")

resultado = tools.ejecutar_seleccion(
    "que hora es"
)

print(resultado)


print()
print("--- INTERNET SIN PERMISO ---")

resultado = tools.ejecutar_seleccion(
    "quiero usar internet"
)

print(resultado)

print(resultado)

