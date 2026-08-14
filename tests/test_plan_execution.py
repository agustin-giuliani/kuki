from brain.tools.manager import ToolManager
from brain.tools.planner import ToolPlanner
from brain.language import LanguageProcessor


tools = ToolManager()
lenguaje = LanguageProcessor()

planner = ToolPlanner(
    tools.catalogo,
    tools.selector
)


print("--- EJECUCION DE PLANES ---")


# -------------------------
# HORA
# -------------------------

entrada = "que hora es"

resultado = lenguaje.procesar(
    entrada
)

plan = planner.planificar(
    entrada,
    resultado
)

print()
print("Plan hora:")
print(plan)

print()
print("Resultado:")

print(
    tools.ejecutar_plan(
        plan
    )
)


# -------------------------
# INTERNET
# -------------------------

entrada = "busca informacion sobre Python"

resultado = lenguaje.procesar(
    entrada
)

plan = planner.planificar(
    entrada,
    resultado
)

print()
print("Plan internet:")
print(plan)

print()
print("Resultado sin permiso:")

print(
    tools.ejecutar_plan(
        plan
    )
)
