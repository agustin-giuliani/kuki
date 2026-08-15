# -*- coding: utf-8 -*-


class SpellCorrector:

    def __init__(self):

        self.palabras_protegidas = {
            "estan",
            "cuales"
        }

        self.vocabulario = {
            "hola",
            "buenas",
            "como",
            "estas",
            "cual",
            "es",
            "tu",
            "nombre",
            "mi",
            "que",
            "hora",
            "busca",
            "buscar",
            "informacion",
            "sobre",
            "python",
            "consulta",
            "consultar",
            "investiga",
            "investigar",
            "internet",
            "herramientas",
            "tenes",
            "tienes",
            "habilitadas",
            "permisos",
            "autorizo",
            "autorizar",
            "permito",
            "rechazo",
            "rechazar",
            "revoco",
            "revocar",
            "utilizar",
            "usar",
            "quiero",
            "necesito",
            "salir"
        }

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

        if palabra in self.vocabulario:
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

        for candidata in self.vocabulario:

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
