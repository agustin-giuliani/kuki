from brain.tools.manager import ToolManager
from brain.tools.selector import ToolSelector


tools = ToolManager()

selector = ToolSelector(
    tools.catalogo
)


print("--- TOOL SELECTOR ---")

entradas = [
    "que hora es",
    "decime la hora",
    "necesito saber la hora",
    "me podes decir la hora actual",
    "quiero consultar internet",
    "busca informacion en internet",
    "necesito informacion de internet",
    "hola",
    "como estas",
    "cual es mi nombre"
]


for entrada in entradas:

    herramienta = selector.seleccionar(
        entrada
    )

    print()
    print("Entrada:", entrada)
    print("Herramienta:", herramienta)
