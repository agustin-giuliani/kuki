from brain.tools.manager import ToolManager
from brain.tools.authorization_planner import AuthorizationPlanner
from brain.tools.authorization_executor import AuthorizationExecutor


tools = ToolManager()

planner = AuthorizationPlanner(
    tools.selector
)

executor = AuthorizationExecutor(
    tools.autorizacion
)


print("--- AUTHORIZATION EXECUTOR ---")


# --------------------------------
# SOLICITAR INTERNET
# --------------------------------

print()
print("Solicitando Internet:")

solicitud = tools.solicitar_permiso(
    "internet"
)

print(solicitud)


# --------------------------------
# PLAN DE APROBACION
# --------------------------------

resultado_lenguaje = {
    "intencion": "autorizar_herramienta",
    "texto": "autorizo internet"
}

plan = planner.planificar(
    resultado_lenguaje
)

print()
print("Plan:")
print(plan)


# --------------------------------
# EJECUTAR APROBACION
# --------------------------------

resultado = executor.ejecutar(
    plan
)

print()
print("Resultado:")
print(resultado)


# --------------------------------
# ESTADO
# --------------------------------

print()
print("Estado del permiso:")

print(
    tools.permissions.listar()
)


# --------------------------------
# REVOCAR PARA DEJAR LIMPIO
# --------------------------------

tools.permissions.revocar(
    "internet"
)
# --------------------------------
# SOLICITAR NUEVAMENTE
# --------------------------------

print()
print("Solicitando Internet nuevamente:")

solicitud = tools.solicitar_permiso(
    "internet"
)

print(solicitud)


# --------------------------------
# PLAN DE RECHAZO
# --------------------------------

resultado_lenguaje = {
    "intencion": "rechazar_herramienta",
    "texto": "rechazo internet"
}

plan = planner.planificar(
    resultado_lenguaje
)

print()
print("Plan de rechazo:")
print(plan)


# --------------------------------
# EJECUTAR RECHAZO
# --------------------------------

resultado = executor.ejecutar(
    plan
)

print()
print("Resultado del rechazo:")
print(resultado)


# --------------------------------
# ESTADO FINAL
# --------------------------------

print()
print("Estado final:")

print(
    tools.permissions.listar()
)