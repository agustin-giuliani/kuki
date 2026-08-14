from brain.tools.manager import ToolManager


tools = ToolManager()


print("--- PLAN MANAGER ---")


# -------------------------
# PLAN HORA
# -------------------------

plan_hora = {
    "necesita_herramienta": True,
    "herramienta": "hora",
    "motivo": "Necesita consultar la hora actual.",
    "datos": {}
}

print()
print("Ejecutando plan de hora:")

print(
    tools.ejecutar_plan(
        plan_hora
    )
)


# -------------------------
# PLAN INTERNET
# -------------------------

plan_internet = {
    "necesita_herramienta": True,
    "herramienta": "internet",
    "motivo": "Necesita informacion externa.",
    "datos": {
        "consulta": "python"
    }
}

print()
print("Ejecutando plan de internet:")

print(
    tools.ejecutar_plan(
        plan_internet
    )
)


# -------------------------
# PLAN SIN HERRAMIENTA
# -------------------------

plan_vacio = {
    "necesita_herramienta": False,
    "herramienta": None,
    "motivo": "No se necesita una herramienta.",
    "datos": {}
}

print()
print("Ejecutando plan sin herramienta:")

print(
    tools.ejecutar_plan(
        plan_vacio
    )
)
