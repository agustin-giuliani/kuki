from brain.tools.permissions import PermissionManager


permisos = PermissionManager()


permisos.registrar(
    "saludar",
    "seguro",
    True
)

permisos.registrar(
    "internet",
    "autorizacion",
    False
)

permisos.registrar(
    "escribir_archivos",
    "alto",
    False
)

permisos.registrar(
    "instalar_software",
    "critico",
    False
)


print("--- PERMISOS DE KUKI ---")

print(
    "Saludar:",
    permisos.tiene_permiso("saludar")
)

print(
    "Nivel:",
    permisos.nivel("saludar")
)

print()

print(
    "Internet:",
    permisos.tiene_permiso("internet")
)

print(
    "Nivel:",
    permisos.nivel("internet")
)

print()

print(
    "Escribir archivos:",
    permisos.tiene_permiso("escribir_archivos")
)

print(
    "Nivel:",
    permisos.nivel("escribir_archivos")
)

print()

print(
    "Instalar software:",
    permisos.tiene_permiso("instalar_software")
)

print(
    "Nivel:",
    permisos.nivel("instalar_software")
)


print()
print("--- CONCEDER INTERNET ---")

permisos.conceder("internet")

print(
    "Internet:",
    permisos.tiene_permiso("internet")
)


print()
print("--- REVOCAR INTERNET ---")

permisos.revocar("internet")

print(
    "Internet:",
    permisos.tiene_permiso("internet")
)