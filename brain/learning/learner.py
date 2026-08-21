# -*- coding: utf-8 -*-


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

        # --------------------------------
        # APRENDIZAJE DE MEMORIA
        # --------------------------------

        if intencion == "aprendizaje_memoria":

            return self._aprender_memoria(
                resultado
            )

        # --------------------------------
        # APRENDIZAJE DE CONOCIMIENTO
        # --------------------------------

        if intencion == "aprendizaje_conocimiento":

            return self._aprender_conocimiento(
                resultado
            )

        # --------------------------------
        # SIN APRENDIZAJE
        # --------------------------------

        return None

    def _aprender_memoria(self, resultado):

        clave = resultado.get(
            "clave"
        )

        valor = resultado.get(
            "valor"
        )

        if not clave or not valor:
            return None

        self.memoria.guardar(
            clave,
            valor
        )

        return "memoria"

    def _aprender_conocimiento(self, resultado):

        clave = resultado.get(
            "clave"
        )

        valor = resultado.get(
            "valor"
        )

        if not clave or not valor:
            return None

        self.conocimiento.guardar(
            clave,
            valor,
            "descripcion"
        )

        return "conocimiento"

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

    def recordar_memoria(self, clave):

        return self.memoria.recordar(
            clave
        )

    def recordar_conocimiento(
        self,
        clave,
        categoria="descripcion"
    ):

        return self.conocimiento.recordar(
            clave,
            categoria
        )