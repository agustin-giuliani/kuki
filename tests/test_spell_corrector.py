from brain.language.spell_corrector import SpellCorrector


corrector = SpellCorrector()


pruebas = [
    "hola",
    "hoal",
    "buenas",
    "buenass",
    "hora",
    "hroa",
    "internet",
    "intrenet",
    "python",
    "xyzabc"
]


print("--- SPELL CORRECTOR ---")


for palabra in pruebas:

    resultado = corrector.corregir_palabra(
        palabra
    )

    print(
        palabra,
        "->",
        resultado
    )


print()
print("--- FRASES ---")


frases = [
    "hoal kuki",
    "que hroa es",
    "busca informacion sobre pyhton",
    "quiero usar intrenet",
    "xyzabc"
]


for frase in frases:

    resultado = corrector.corregir(
        frase
    )

    print(
        frase,
        "->",
        resultado
    )

print()
print("--- CANDIDATOS ---")

pruebas_candidatos = [
    "hoal",
    "hroa",
    "pyhton",
    "intrenet",
    "bl3nder",
    "xyzabc"
]

for palabra in pruebas_candidatos:

    candidatos = corrector.buscar_candidatos(
        palabra
    )

    print(
        palabra,
        "->",
        candidatos
    )

print()
print("--- ANALISIS ---")

pruebas_analisis = [
    "hola",
    "hoal",
    "hroa",
    "pyhton",
    "intrenet",
    "bl3nder",
    "xyzabc"
]

for palabra in pruebas_analisis:

    resultado = corrector.analizar_palabra(
        palabra
    )

    print(
        palabra,
        "->",
        resultado
    )