from brain.tools.manager import ToolManager
from brain.tools.authorization_planner import AuthorizationPlanner


tools = ToolManager()

planner = AuthorizationPlanner(
    tools.selector
)


print("--- AUTHORIZATION PLANNER ---")


casos = [

    {
        "intencion": "autorizar_herramienta",
        "texto": "autorizo internet"
    },

    {
        "intencion": "revocar_herramienta",
        "texto": "revoco internet"
    },

    {
        "intencion": "rechazar_herramienta",
        "texto": "rechazo internet"
    },

    {
        "intencion": "saludo",
        "texto": "hola"
    }

]


for caso in casos:

    print()
    print("Entrada:")
    print(caso)

    plan = planner.planificar(
        caso
    )

    print("Plan:")
    print(plan)