from brain.tools.manager import ToolManager


tools = ToolManager()


print("--- SISTEMA DE AUTORIZACION ---")


print()
print("Solicitando Internet:")

resultado = tools.solicitar_permiso(
    "internet"
)

print(resultado)


print()
print("Solicitudes pendientes:")

print(
    tools.listar_solicitudes()
)


print()
print("Estado del permiso:")

print(
    tools.permissions.obtener_info(
        "internet"
    )
)

print()
print("--- APROBAR INTERNET ---")

resultado = tools.autorizacion.aprobar(
    "internet"
)

print(resultado)


print()
print("Estado del permiso despues de aprobar:")

print(
    tools.permissions.obtener_info(
        "internet"
    )
)


print()
print("--- HISTORIAL DE PERMISOS ---")

for evento in tools.permissions.obtener_historial():

    print(evento)


print()
print("--- REVOCAR INTERNET ---")

tools.permissions.revocar(
    "internet",
    origen="usuario"
)

print(
    tools.permissions.obtener_info(
        "internet"
    )
)

print()
print("--- HISTORIAL FINAL ---")

for evento in tools.permissions.obtener_historial():

    print(evento)

print()
print("--- SOLICITUD DUPLICADA ---")

tools.permissions.revocar(
    "internet",
    origen="usuario"
)

primera = tools.solicitar_permiso(
    "internet"
)

segunda = tools.solicitar_permiso(
    "internet"
)

print("Primera:", primera)
print("Segunda:", segunda)

print()
print("--- PRUEBA DE SEGURIDAD ---")

print()
print("KUKI intenta aprobar Internet:")

print(
    tools.autorizacion.aprobar(
        "internet",
        origen="kuki"
    )
)

print()
print("KUKI intenta rechazar Internet:")

print(
    tools.autorizacion.rechazar(
        "internet",
        origen="kuki"
    )
)