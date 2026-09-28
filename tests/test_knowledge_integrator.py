import os

from brain.learning.knowledge import Knowledge
from brain.learning.knowledge_integrator import KnowledgeIntegrator


# --------------------------------
# LIMPIAR ARCHIVO DE PRUEBA
# --------------------------------

if os.path.exists(
    "data/test_integrator_knowledge.json"
):

    os.remove(
        "data/test_integrator_knowledge.json"
    )


# --------------------------------
# CREAR COMPONENTES
# --------------------------------

conocimiento = Knowledge(
    "data/test_integrator_knowledge.json"
)

integrador = KnowledgeIntegrator(
    conocimiento
)


print("--- KNOWLEDGE INTEGRATOR ---")


# --------------------------------
# INTEGRAR CONOCIMIENTO NUEVO
# --------------------------------

print()
print("Integrar conocimiento nuevo:")

print(
    integrador.integrar(
        "java",
        "lenguaje de programacion",
        [
            {
                "tipo": "internet",
                "url": "https://ejemplo.com/java"
            }
        ]
    )
)


# --------------------------------
# MOSTRAR CONOCIMIENTO NUEVO
# --------------------------------

print()
print("Conocimiento nuevo:")

print(
    conocimiento.obtener(
        "java"
    )
)


# --------------------------------
# CREAR CONOCIMIENTO BASE
# --------------------------------

print()
print("Crear conocimiento base:")

print(
    conocimiento.guardar(
        "python",
        "lenguaje de programacion de alto nivel",
        "descripcion"
    )
)


# --------------------------------
# INTEGRAR NUEVO DATO
# --------------------------------

print()
print("Integrar nuevo dato:")

print(
    integrador.integrar(
        "python",
        "interpretado y de proposito general",
        [
            {
                "tipo": "internet",
                "url": "https://ejemplo.com/python"
            }
        ]
    )
)


# --------------------------------
# INTEGRAR OTRO DATO
# --------------------------------

print()
print("Integrar segundo dato:")

print(
    integrador.integrar(
        "python",
        "codigo claro y facil de leer",
        [
            {
                "tipo": "github",
                "url": "https://github.com/ejemplo/python"
            }
        ]
    )
)


# --------------------------------
# REPETIR DATO
# --------------------------------

print()
print("Repetir primer dato:")

print(
    integrador.integrar(
        "python",
        "interpretado y de proposito general",
        [
            {
                "tipo": "internet",
                "url": "https://otro-sitio.com/python"
            }
        ]
    )
)


# --------------------------------
# MOSTRAR CONOCIMIENTO
# --------------------------------

print()
print("Conocimiento final:")

print(
    conocimiento.obtener(
        "python"
    )
)


# --------------------------------
# MOSTRAR ARCHIVO
# --------------------------------

print()
print("Archivo final:")

with open(
    "data/test_integrator_knowledge.json",
    "r",
    encoding="utf-8"
) as archivo:

    print(
        archivo.read()
    )