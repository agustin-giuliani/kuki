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
