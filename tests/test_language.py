
from brain.language import LanguageProcessor


lenguaje = LanguageProcessor()

print("--- PROCESADOR DE LENGUAJE DE KUKI ---")

frases = [
    "Hola KUKI",
    "Buenas",
    "Como estas",
    "Cual es tu nombre",
    "Que hora es"
]

for frase in frases:

    resultado = lenguaje.procesar(frase)

    print(
        "Entrada:", frase,
        "| Intencion:", resultado["intencion"]
    )
