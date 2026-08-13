from brain.memory import Memory
from brain.knowledge import Knowledge
from brain.learning import Learning


memoria = Memory()
conocimiento = Knowledge()

aprendizaje = Learning(memoria)

print("--- APRENDIZAJE DE KUKI ---")

# Informacion personal
frase_personal = "Mi comida favorita es la pizza"

aprendio = aprendizaje.aprender_frase(frase_personal)

if aprendio:
    print(
        "Memoria personal:",
        memoria.recordar("comida favorita")
    )
else:
    print("KUKI no pudo aprender la informacion personal.")


# Conocimiento general
frase_conocimiento = "Python es un lenguaje de programacion"

aprendio = aprendizaje.aprender_frase(frase_conocimiento)

if aprendio:
    print(
        "Conocimiento:",
        conocimiento.recordar("python")
    )
else:
    print("KUKI no pudo aprender el conocimiento.")