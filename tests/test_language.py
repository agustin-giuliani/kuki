
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
    "Para que sirve Python?",
    "Quiero consultar internet",
    "Necesito internet",
    "Busca en internet",
    "Consulta internet"
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

print(
    "Autorizo internet",
    "->",
    lenguaje.procesar("Autorizo internet")["intencion"]
)

print(
    "Permito usar internet",
    "->",
    lenguaje.procesar("Permito usar internet")["intencion"]
)

print(
    "Rechazo internet",
    "->",
    lenguaje.procesar("Rechazo internet")["intencion"]
)

print(
    "No permito internet",
    "->",
    lenguaje.procesar("No permito internet")["intencion"]
)

print(
    "Busca informacion sobre Python ->",
    lenguaje.procesar(
        "Busca informacion sobre Python"
    )
)

print(
    "Investiga sobre Python ->",
    lenguaje.procesar(
        "Investiga sobre Python"
    )
)

print(
    "Revoco internet ->",
    lenguaje.procesar(
        "Revoco internet"
    )["intencion"]
)

print(
    "Revocar internet ->",
    lenguaje.procesar(
        "Revocar internet"
    )["intencion"]
)

print(
    "Revoca internet ->",
    lenguaje.procesar(
        "Revoca internet"
    )["intencion"]
)