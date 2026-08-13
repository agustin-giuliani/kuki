from brain.memory import Memory
from brain.learning import Learning


memoria = Memory()
aprendizaje = Learning(memoria)

print("--- APRENDIZAJE DE KUKI ---")

frase = "Mi comida favorita es la pizza"

aprendio = aprendizaje.aprender_frase(frase)

if aprendio:
    print("KUKI aprendio:", memoria.recordar("comida favorita"))
else:
    print("KUKI no pudo aprender la frase.")
