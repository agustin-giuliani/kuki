# -*- coding: utf-8 -*-

import re


class TextNormalizer:

    def normalizar(self, texto):

        if texto is None:
            return ""

        texto = texto.lower().strip()

        # Reemplazar signos de puntuacion
        texto = re.sub(
            r"[?!.,;:]",
            "",
            texto
        )

        # Eliminar espacios repetidos
        texto = re.sub(
            r"\s+",
            " ",
            texto
        )

        return texto.strip()
