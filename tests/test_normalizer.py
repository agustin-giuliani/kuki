# -*- coding: utf-8 -*-

from brain.normalizer import TextNormalizer


normalizador = TextNormalizer()


pruebas = [
    "Hola KUKI",
    "  Hola KUKI  ",
    "Que hora es?",
    "BUSCA INFORMACION SOBRE PYTHON!",
    "   que    herramientas   tenes   ",
    "Buenas!",
]


print("--- TEXT NORMALIZER ---")


for texto in pruebas:

    resultado = normalizador.normalizar(
        texto
    )

    print(
        "Entrada:",
        repr(texto)
    )

    print(
        "Resultado:",
        repr(resultado)
    )

    print()