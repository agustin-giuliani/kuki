
from brain.language import LanguageProcessor


lenguaje = LanguageProcessor()

print("--- PROCESADOR DE LENGUAJE DE KUKI ---")

frases = [
    "Hola KUKI",
    "Buenas",
    "Como estas",
    "Cual es tu nombre",
    "Que hora es",
    "Cual es mi comida favorita?",
    "Mi color favorito es negro",
    "Python es un lenguaje de programacion",
    "Que es Python?",
    "Para que sirve Python?"
]

for frase in frases:

    resultado = lenguaje.procesar(frase)

    print(
        "Entrada:", frase,
        "| Intencion:", resultado["intencion"]
    )

print(
    "Entrada: Y para que sirve? | Intencion:",
    lenguaje.procesar("Y para que sirve?")["intencion"]
)