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

    # --------------------------------
    # APRENDER MEMORIA
    # --------------------------------

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

    # --------------------------------
    # APRENDER CONOCIMIENTO
    # --------------------------------

    def _aprender_conocimiento(self, resultado):

        clave = resultado.get(
            "clave"
        )

        valor = resultado.get(
            "valor"
        )

        if not clave or not valor:
            return None

        # --------------------------------
        # EVALUAR CONOCIMIENTO
        # --------------------------------

        evaluacion = self._evaluar_conocimiento(
            clave,
            valor
        )

        # --------------------------------
        # GUARDAR CONOCIMIENTO NUEVO
        # --------------------------------

        if evaluacion == "conocimiento":

            self.conocimiento.guardar(
                clave,
                valor,
                "descripcion"
            )

        return evaluacion

    # --------------------------------
    # EVALUAR CONOCIMIENTO
    # --------------------------------

    def _evaluar_conocimiento(
        self,
        clave,
        valor
    ):

        if not clave or not valor:
            return None

        # --------------------------------
        # OBTENER CONOCIMIENTO EXISTENTE
        # --------------------------------

        conocimiento_existente = self.conocimiento.obtener(
            clave
        )

        # --------------------------------
        # CONOCIMIENTO NUEVO
        # --------------------------------

        if conocimiento_existente is None:

            return "conocimiento"

        # --------------------------------
        # OBTENER DESCRIPCION EXISTENTE
        # --------------------------------

        descripcion_existente = conocimiento_existente.get(
            "descripcion"
        )

        # --------------------------------
        # CONOCIMIENTO IGUAL
        # --------------------------------

        if descripcion_existente == valor:

            return "conocimiento_igual"

        # --------------------------------
        # INFORMACION DIFERENTE
        # --------------------------------

        return "conocimiento_nuevo_dato"

    # --------------------------------
    # APRENDER DESDE UNA FRASE
    # --------------------------------

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

    # --------------------------------
    # RECORDAR MEMORIA
    # --------------------------------

    def recordar_memoria(self, clave):

        return self.memoria.recordar(
            clave
        )

    # --------------------------------
    # RECORDAR CONOCIMIENTO
    # --------------------------------

    def recordar_conocimiento(
        self,
        clave,
        categoria="descripcion"
    ):

        return self.conocimiento.recordar(
            clave,
            categoria
        )

    # --------------------------------
    # APRENDIZAJE EXTERNO
    # --------------------------------

    def aprender_externo(self, resultado_tool):

        if not resultado_tool:
            return None

        if resultado_tool.get("estado") != "ok":
            return None

        resultado = resultado_tool.get(
            "resultado"
        )

        if not resultado:
            return None

        resultados = resultado.get(
            "resultados"
        )

        if not resultados:
            return None

        primer_resultado = resultados[0]

        if not primer_resultado:
            return None

        clave = primer_resultado.get(
            "titulo"
        )

        descripcion = primer_resultado.get(
            "descripcion"
        )

        url = primer_resultado.get(
            "url"
        )

        if not clave or not descripcion:
            return None

        self.conocimiento.guardar(
            clave,
            descripcion,
            "descripcion"
        )

        self.conocimiento.agregar_fuente(
            clave,
            "internet",
            url
        )

        return "conocimiento"