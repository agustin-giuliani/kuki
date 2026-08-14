from brain.tools.manager import ToolManager
from brain.tools.planner import ToolPlanner
from brain.language import LanguageProcessor


tools = ToolManager()
lenguaje = LanguageProcessor()

planner = ToolPlanner(
    tools.selector
)


print("--- TOOL PLANNER ---")


entradas = [
    "que hora es",
    "busca informacion sobre Python",
    "quiero usar internet",
    "hola",
    "cual es mi nombre"
]


for entrada in entradas:

    resultado = lenguaje.procesar(
        entrada
    )

    plan = planner.planificar(
        entrada,
        resultado
    )

    print()
    print("Entrada:", entrada)
    print("Lenguaje:", resultado)
    print("Plan:", plan)
