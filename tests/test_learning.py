from brain.learning.learner import Learning
from brain.learning.memory import Memory
from brain.learning.knowledge import Knowledge


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