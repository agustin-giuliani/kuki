# -*- coding: utf-8 -*-

from brain.language.vocabulary import Vocabulary
from brain.language.variant_detector import VariantDetector


vocabulario = Vocabulary()

vocabulario.registrar(
    "blender",
    origen="base"
)

vocabulario.registrar(
    "python",
    origen="base"
)

vocabulario.registrar(
    "hola",
    origen="base"
)


detector = VariantDetector(
    vocabulario
)


print("--- VARIANT DETECTOR ---")


pruebas = [
    "blender",
    "bl3nder",
    "python",
    "pyth0n",
    "hola",
    "h0la",
    "xyzabc",
    "123abc",
    "bl3nder",
    "pyth0n",
    "h0la",
    "bl5nder",
    "pyt3on",
    "123abc",
    "3d",
    "mp3"
]


for palabra in pruebas:

    resultado = detector.detectar(
        palabra
    )

    print(
        palabra,
        "->",
        resultado
    )
