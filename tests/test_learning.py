# -*- coding: utf-8 -*-

import os

from brain.learning.learner import Learning
from brain.learning.memory import Memory
from brain.learning.knowledge import Knowledge
from brain.learning.pending_knowledge import PendingKnowledge
from brain.learning.knowledge_integrator import KnowledgeIntegrator
from brain.learning.memory_integrator import MemoryIntegrator


# --------------------------------
# LIMPIAR ARCHIVOS DE PRUEBA
# --------------------------------

# Eliminamos los archivos utilizados por
# las pruebas anteriores para empezar
# siempre desde un estado limpio.
if os.path.exists("data/test_memory.json"):
    os.remove("data/test_memory.json")

if os.path.exists("data/test_knowledge.json"):
    os.remove("data/test_knowledge.json")

if os.path.exists("data/test_pending_knowledge.json"):
    os.remove("data/test_pending_knowledge.json")


# --------------------------------
# CREAR COMPONENTES DE PRUEBA
# --------------------------------

# Memory se encarga del almacenamiento
# de los recuerdos.
memoria = Memory(
    "data/test_memory.json"
)

# Knowledge se encarga del almacenamiento
# del conocimiento general.
conocimiento = Knowledge(
    "data/test_knowledge.json"
)

# PendingKnowledge almacena información
# externa que todavía no fue validada.
pending_knowledge = PendingKnowledge(
    "data/test_pending_knowledge.json"
)

# KnowledgeIntegrator decide cómo integrar
# nueva información al conocimiento existente.
knowledge_integrator = KnowledgeIntegrator(
    conocimiento
)

# MemoryIntegrator decide cómo organizar
# la información personal antes de guardarla.
memory_integrator = MemoryIntegrator(
    memoria
)

# Learning ahora recibe ambos integradores:
#
# MemoryIntegrator -> memoria
# KnowledgeIntegrator -> conocimiento
#
# De esta forma Learning coordina el aprendizaje
# pero no necesita conocer los detalles
# de cómo se almacena cada tipo de información.
learning = Learning(
    memoria,
    conocimiento,
    pending_knowledge,
    knowledge_integrator,
    memory_integrator
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
# RECORDAR MEMORIA MEDIANTE LEARNING
# --------------------------------

print()
print("Recordar color mediante Learning:")

print(
    learning.recordar_memoria(
        "color favorito"
    )
)


print()
print("Recordar nombre mediante Learning:")

print(
    learning.recordar_memoria(
        "nombre"
    )
)


print()
print("Recordar campo especifico:")

print(
    learning.recordar_memoria(
        "nombre",
        "categoria"
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

print(
    "Recordar Python desde pendientes:",
    pending_knowledge.obtener(
        "Python"
    )
)


# --------------------------------
# MISMA INFORMACION DESDE OTRA FUENTE
# --------------------------------

resultado_externo_2 = {
    "estado": "ok",
    "resultado": {
        "consulta": "python",
        "resultados": [
            {
                "titulo": "Python",
                "descripcion": "lenguaje de programacion de alto nivel",
                "url": "https://github.com/ejemplo/python"
            }
        ]
    }
}


print()
print("Misma informacion desde otra fuente:")

print(
    learning.aprender_externo(
        resultado_externo_2
    )
)

print(
    "Pendientes despues de segunda fuente:",
    pending_knowledge.obtener(
        "Python"
    )
)


# --------------------------------
# VALIDAR CONOCIMIENTO PENDIENTE
# --------------------------------

print()
print("Validar conocimiento pendiente:")

print(
    learning.validar_conocimiento(
        "python",
        "lenguaje de programacion de alto nivel"
    )
)


print(
    "Python despues de validar:",
    conocimiento.recordar(
        "Python"
    )
)


print(
    "Pendientes despues de validar:",
    pending_knowledge.obtener(
        "Python"
    )
)


# --------------------------------
# MOSTRAR ARCHIVO DE MEMORIA
# --------------------------------

print()
print("Estado final de la memoria:")

with open(
    "data/test_memory.json",
    "r",
    encoding="utf-8"
) as archivo:

    print(
        archivo.read()
    )


# --------------------------------
# MOSTRAR ARCHIVO DE CONOCIMIENTO
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