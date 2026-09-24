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

    # --------------------------------
    # APRENDIZAJE EXTERNO
    # --------------------------------

    def aprender_externo(self, resultado_tool):

        # Verificamos que exista un resultado
        if not resultado_tool:
            return None

        # La herramienta debe haber terminado correctamente
        if resultado_tool.get("estado") != "ok":
            return None

        resultado = resultado_tool.get(
            "resultado"
        )

        if not resultado:
            return None

        # Obtenemos los resultados encontrados
        resultados = resultado.get(
            "resultados"
        )

        if not resultados:
            return None

        # Por ahora aprendemos del primer resultado.
        # Más adelante podremos analizar varios resultados.
        primer_resultado = resultados[0]

        if not primer_resultado:
            return None

        clave = primer_resultado.get(
            "titulo"
        )

        descripcion = primer_resultado.get(
            "descripcion"
        )

        if not clave or not descripcion:
            return None

        # Guardamos la información como conocimiento general.
        self.conocimiento.guardar(
            clave,
            descripcion,
            "descripcion"
        )

        return "conocimiento"