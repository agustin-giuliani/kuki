import os

from brain.learning.pending_knowledge import PendingKnowledge


# --------------------------------
# LIMPIAR ARCHIVO DE PRUEBA
# --------------------------------

if os.path.exists(
    "data/test_pending_knowledge.json"
):

    os.remove(
        "data/test_pending_knowledge.json"
    )


# --------------------------------
# CREAR PENDING KNOWLEDGE
# --------------------------------

pending = PendingKnowledge(
    "data/test_pending_knowledge.json"
)


print("--- PENDING KNOWLEDGE ---")


# --------------------------------
# NUEVO CONOCIMIENTO
# --------------------------------

print()
print("Agregar conocimiento pendiente:")

print(
    pending.guardar(
        "Python",
        "lenguaje de programacion de alto nivel",
        "internet",
        "https://ejemplo.com/python"
    )
)


# --------------------------------
# COMPROBAR EXISTENCIA
# --------------------------------

print()
print("Existe Python:")

print(
    pending.existe(
        "python"
    )
)


print()
print("Existe afirmacion:")

print(
    pending.existe(
        "python",
        "lenguaje de programacion de alto nivel"
    )
)


# --------------------------------
# REPETIR MISMA AFIRMACION
# --------------------------------

print()
print("Repetir misma afirmacion:")

print(
    pending.guardar(
        "python",
        "lenguaje de programacion de alto nivel",
        "github",
        "https://github.com/ejemplo/python"
    )
)


# --------------------------------
# OTRA AFIRMACION
# --------------------------------

print()
print("Agregar otra afirmacion:")

print(
    pending.guardar(
        "python",
        "Python fue creado por Guido van Rossum",
        "internet",
        "https://otro-sitio.com/python"
    )
)


# --------------------------------
# MOSTRAR PENDIENTES
# --------------------------------

print()
print("Pendientes de Python:")

print(
    pending.obtener(
        "python"
    )
)


# --------------------------------
# ELIMINAR UNA AFIRMACION
# --------------------------------

print()
print("Eliminar primera afirmacion:")

print(
    pending.eliminar(
        "python",
        "lenguaje de programacion de alto nivel"
    )
)


# --------------------------------
# MOSTRAR ESTADO FINAL
# --------------------------------

print()
print("Estado final:")

print(
    pending.obtener(
        "python"
    )
)


# --------------------------------
# MOSTRAR ARCHIVO
# --------------------------------

print()
print("Archivo final:")

with open(
    "data/test_pending_knowledge.json",
    "r",
    encoding="utf-8"
) as archivo:

    print(
        archivo.read()
    )
