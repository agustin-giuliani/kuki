
from brain.language.processor import LanguageProcessor


lenguaje = LanguageProcessor()

print("--- VARIANTES EN LANGUAGE PROCESSOR ---")

resultado = lenguaje.procesar(
    "bl3nder"
)

print(resultado)

resultado = lenguaje.procesar(
    "pyth0n"
)

print(resultado)

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

print(
    "Que herramientas tenes ->",
    lenguaje.procesar(
        "Que herramientas tenes"
    )["intencion"]
)

print(
    "Que permisos tenes ->",
    lenguaje.procesar(
        "Que permisos tenes"
    )["intencion"]
)

print(
    "Que herramientas estan habilitadas ->",
    lenguaje.procesar(
        "Que herramientas estan habilitadas"
    )["intencion"]
)

print(
    "Cuales son tus permisos ->",
    lenguaje.procesar(
        "Cuales son tus permisos"
    )["intencion"]
)

pruebas = [
    "BUSCA INFORMACION SOBRE PYTHON!!!!!!",
    "QUE HORA ES???",
    "HOLA KUKI!!!!!"
]


print("--- NORMALIZACION + LENGUAJE ---")


for texto in pruebas:

    resultado = lenguaje.procesar(texto)

    print()
    print("Entrada:", texto)
    print("Resultado:", resultado)

pruebas_permisos = [
    "Que herramientas tenes",
    "Que permisos tenes",
    "Que herramientas estan habilitadas",
    "Cuales son tus permisos"
]

print("--- PERMISOS ---")

for entrada in pruebas_permisos:

    resultado = lenguaje.procesar(
        entrada
    )

    print(
        entrada,
        "->",
        resultado
    )

print()
print("--- DATOS DE APRENDIZAJE ---")

resultado = lenguaje.procesar(
    "Mi color favorito es negro"
)

print(resultado)

resultado = lenguaje.procesar(
    "Me llamo Agustin"
)

print(resultado)

resultado = lenguaje.procesar(
    "Python es un lenguaje de programacion"
)

print(resultado)