from brain.tools.manager import ToolManager


tools = ToolManager()


print("--- TOOL MANAGER AUTHORIZATION ---")


# --------------------------------
# SOLICITAR
# --------------------------------

print()
print("Solicitando Internet:")

print(
    tools.solicitar_permiso(
        "internet"
    )
)


# --------------------------------
# AUTORIZAR
# --------------------------------

print()
print("Autorizando Internet:")

resultado = tools.ejecutar_autorizacion(
    {
        "intencion": "autorizar_herramienta",
        "texto": "autorizo internet"
    }
)

print(resultado)


# --------------------------------
# ESTADO
# --------------------------------

print()
print("Estado:")

print(
    tools.permissions.listar()
)


# --------------------------------
# REVOCAR
# --------------------------------

tools.permissions.revocar(
    "internet"
)
