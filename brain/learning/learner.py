# -*- coding: utf-8 -*-

from .knowledge import Knowledge


class Learning:

    def __init__(self, memoria, conocimiento):

        self.memoria = memoria
        self.conocimiento = conocimiento

    def aprender(self, resultado):

        if not resultado:
            return None

        intencion = resultado.get(
            "intencion"
        )

        clave = resultado.get(
            "clave"
        )

        valor = resultado.get(
            "valor"
        )

        if not clave or not valor:
            return None

        # --------------------------------
        # APRENDIZAJE DE MEMORIA
        # --------------------------------

        if intencion == "aprendizaje_memoria":

            self.memoria.guardar(
                clave,
                valor
            )

            return "memoria"

        # --------------------------------
        # APRENDIZAJE DE CONOCIMIENTO
        # --------------------------------

        if intencion == "aprendizaje_conocimiento":

            self.conocimiento.guardar(
                clave,
                valor,
                "descripcion"
            )

            return "conocimiento"

        return None

    def aprender_frase(self, texto):

        texto = texto.lower().strip()

        # --------------------------------
        # NO APRENDER PREGUNTAS
        # --------------------------------

        if texto.startswith("que es "):
            return None

        if texto.startswith("cual es "):
            return None

        # --------------------------------
        # APRENDER NOMBRE
        # --------------------------------

        if texto.startswith("me llamo "):

            nombre = texto[9:].strip()

            if nombre:

                self.memoria.guardar(
                    "nombre",
                    nombre
                )

                return "memoria"

        # --------------------------------
        # FRASE DE CONOCIMIENTO
        # --------------------------------

        if " es " not in texto:
            return None

        clave, valor = texto.split(
            " es ",
            1
        )

        clave = clave.strip()
        valor = valor.strip().rstrip(".")

        if not clave or not valor:
            return None

        # --------------------------------
        # INFORMACION PERSONAL
        # --------------------------------

        if texto.startswith("mi "):

            clave = clave[3:].strip()

            if clave.startswith("cual"):
                return None

            self.memoria.guardar(
                clave,
                valor
            )

            return "memoria"

        # --------------------------------
        # CONOCIMIENTO GENERAL
        # --------------------------------

        self.conocimiento.guardar(
            clave,
            valor,
            "descripcion"
        )

        return "conocimiento"