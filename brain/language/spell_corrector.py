# -*- coding: utf-8 -*-
from brain.language.vocabulary import Vocabulary
from brain.language.vocabulary_base import PALABRAS_BASE

class SpellCorrector:

    def __init__(self, vocabulario=None):

        if vocabulario is None:
            vocabulario = Vocabulary()

        self.vocabulario = vocabulario

        self.palabras_protegidas = {
            "estan",
            "cuales"
        }

        self.vocabulario.registrar_muchas(
            PALABRAS_BASE,
            origen="base"
        )

    def distancia(self, palabra1, palabra2):

        longitud1 = len(palabra1)
        longitud2 = len(palabra2)

        matriz = []

        for i in range(longitud1 + 1):

            matriz.append(
                [0] * (longitud2 + 1)
            )

        for i in range(longitud1 + 1):
            matriz[i][0] = i

        for j in range(longitud2 + 1):
            matriz[0][j] = j

        for i in range(1, longitud1 + 1):

            for j in range(1, longitud2 + 1):

                costo = 0

                if palabra1[i - 1] != palabra2[j - 1]:
                    costo = 1

                matriz[i][j] = min(
                    matriz[i - 1][j] + 1,
                    matriz[i][j - 1] + 1,
                    matriz[i - 1][j - 1] + costo
                )

                # --------------------------------
                # TRANSPOSICION
                # --------------------------------

                if (
                    i > 1
                    and j > 1
                    and palabra1[i - 1] == palabra2[j - 2]
                    and palabra1[i - 2] == palabra2[j - 1]
                ):

                    matriz[i][j] = min(
                        matriz[i][j],
                        matriz[i - 2][j - 2] + 1
                    )

        return matriz[longitud1][longitud2]

    def corregir_palabra(self, palabra):

        if self.vocabulario.conoce(palabra):
            return palabra

        if palabra in self.palabras_protegidas:
            return palabra


        longitud = len(palabra)

        if longitud <= 3:
            return palabra

        if longitud <= 5:
            distancia_maxima = 1
        else:
            distancia_maxima = 2

        candidatos = []

        for candidata in self.vocabulario.listar():

            distancia = self.distancia(
                palabra,
                candidata
            )

            if distancia <= distancia_maxima:

                candidatos.append(
                    (
                        candidata,
                        distancia
                    )
                )

        if not candidatos:
            return palabra

        # --------------------------------
        # SOLO CORREGIMOS SI HAY
        # UNA CANDIDATA CLARA
        # --------------------------------

        candidatos.sort(
            key=lambda elemento: elemento[1]
        )

        mejor_distancia = candidatos[0][1]

        mejores = [
            candidata
            for candidata, distancia
            in candidatos
            if distancia == mejor_distancia
        ]

        # Si hay empate, no adivinamos.
        if len(mejores) != 1:
            return palabra

        return mejores[0]

    def corregir(self, texto):

        palabras = texto.split()

        resultado = []

        for palabra in palabras:

            palabra_corregida = self.corregir_palabra(
                palabra
            )

            resultado.append(
                palabra_corregida
            )

        return " ".join(resultado)
