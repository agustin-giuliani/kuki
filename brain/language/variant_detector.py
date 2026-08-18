# -*- coding: utf-8 -*-


class VariantDetector:

    def __init__(self, vocabulario):

        self.vocabulario = vocabulario

        self.mapa_variantes = {
            "0": "o",
            "3": "e"
        }

    def normalizar_variante(self, palabra):

        palabra = palabra.lower().strip()

        resultado = []
        cambios = 0

        for caracter in palabra:

            if caracter in self.mapa_variantes:

                resultado.append(
                    self.mapa_variantes[caracter]
                )

                cambios += 1

            else:

                resultado.append(
                    caracter
                )

        return {
            "texto": "".join(resultado),
            "cambios": cambios
        }

    def detectar(self, palabra):

        palabra = palabra.lower().strip()

        if not palabra:

            return {
                "estado": "vacia",
                "palabra": palabra,
                "normalizada": "",
                "candidato": None,
                "cambios": 0
            }

        if self.vocabulario.conoce(palabra):

            return {
                "estado": "conocida",
                "palabra": palabra,
                "normalizada": palabra,
                "candidato": palabra,
                "cambios": 0
            }

        resultado_normalizacion = self.normalizar_variante(
            palabra
        )

        normalizada = resultado_normalizacion["texto"]
        cambios = resultado_normalizacion["cambios"]

        if cambios == 0:

            return {
                "estado": "sin_variante",
                "palabra": palabra,
                "normalizada": normalizada,
                "candidato": None,
                "cambios": 0
            }

        if self.vocabulario.conoce(normalizada):

            return {
                "estado": "variante_probable",
                "palabra": palabra,
                "normalizada": normalizada,
                "candidato": normalizada,
                "cambios": cambios
            }

        return {
            "estado": "desconocida",
            "palabra": palabra,
            "normalizada": normalizada,
            "candidato": None,
            "cambios": cambios
        }