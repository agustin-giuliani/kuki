import os

from brain.learning.learner import Learning
from brain.learning.memory import Memory
from brain.learning.knowledge import Knowledge


# --------------------------------
# LIMPIAR ARCHIVOS DE PRUEBA
# --------------------------------

if os.path.exists("data/test_memory.json"):
    os.remove("data/test_memory.json")

if os.path.exists("data/test_knowledge.json"):
    os.remove("data/test_knowledge.json")


# --------------------------------
# CREAR COMPONENTES DE PRUEBA
# --------------------------------

memoria = Memory(
    "data/test_memory.json"
)

conocimiento = Knowledge(
    "data/test_knowledge.json"
)

learning = Learning(
    memoria,
    conocimiento
)


print("--- LEARNING ---")


# --------------------------------
# APRENDIZAJE DE MEMORIA
# --------------------------------

resultado_memoria = {
    "intencion": "aprendizaje_memoria",
    "tipo": "dato_usuario",
    "clave": "color favorito",
    "valor": "negro",
    "texto": "mi color favorito es negro"
}


print()
print("Aprender memoria:")

print(
    learning.aprender(
        resultado_memoria
    )
)

print(
    "Recordar color:",
    memoria.recordar(
        "color favorito"
    )
)


# --------------------------------
# APRENDIZAJE DEL NOMBRE
# --------------------------------

resultado_nombre = {
    "intencion": "aprendizaje_memoria",
    "tipo": "nombre",
    "clave": "nombre",
    "valor": "agustin",
    "texto": "me llamo agustin"
}


print()
print("Aprender nombre:")

print(
    learning.aprender(
        resultado_nombre
    )
)

print(
    "Recordar nombre:",
    memoria.recordar(
        "nombre"
    )
)


# --------------------------------
# APRENDIZAJE DE CONOCIMIENTO
# --------------------------------

resultado_conocimiento = {
    "intencion": "aprendizaje_conocimiento",
    "tipo": "conocimiento",
    "clave": "python",
    "valor": "un lenguaje de programacion",
    "texto": "python es un lenguaje de programacion"
}


print()
print("Aprender conocimiento:")

print(
    learning.aprender(
        resultado_conocimiento
    )
)

print(
    "Recordar Python:",
    conocimiento.recordar(
        "python"
    )
)


# --------------------------------
# CONOCIMIENTO EXISTENTE
# --------------------------------

resultado_conocimiento_existente = {
    "intencion": "aprendizaje_conocimiento",
    "tipo": "conocimiento",
    "clave": "Python",
    "valor": "un lenguaje de programacion de alto nivel",
    "texto": "Python es un lenguaje de programacion de alto nivel"
}


print()
print("Aprender conocimiento existente:")

print(
    learning.aprender(
        resultado_conocimiento_existente
    )
)

print(
    "Descripcion despues:",
    conocimiento.recordar(
        "python"
    )
)


# --------------------------------
# CONOCIMIENTO IGUAL
# --------------------------------

resultado_conocimiento_igual = {
    "intencion": "aprendizaje_conocimiento",
    "tipo": "conocimiento",
    "clave": "Python",
    "valor": "un lenguaje de programacion",
    "texto": "Python es un lenguaje de programacion"
}


print()
print("Aprender conocimiento igual:")

print(
    learning.aprender(
        resultado_conocimiento_igual
    )
)

print(
    "Descripcion despues:",
    conocimiento.recordar(
        "python"
    )
)


# --------------------------------
# APRENDIZAJE DESDE INTERNET
# --------------------------------

resultado_externo = {
    "estado": "ok",
    "resultado": {
        "consulta": "python",
        "resultados": [
            {
                "titulo": "Python",
                "descripcion": "lenguaje de programacion de alto nivel",
                "url": "https://es.wikipedia.org/wiki/Python"
            }
        ]
    }
}


print()
print("Aprender desde fuente externa:")

print(
    learning.aprender_externo(
        resultado_externo
    )
)

print(
    "Recordar Python desde conocimiento:",
    conocimiento.recordar(
        "Python"
    )
)


# --------------------------------
# MOSTRAR ARCHIVO DE PRUEBA
# --------------------------------

print()
print("Estado final del conocimiento:")

with open(
    "data/test_knowledge.json",
    "r",
    encoding="utf-8"
) as archivo:

    print(
        archivo.read()
    )