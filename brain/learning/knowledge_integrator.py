# -*- coding: utf-8 -*-


class KnowledgeIntegrator:

    def __init__(self, conocimiento):

        self.conocimiento = conocimiento

    # --------------------------------
    # NORMALIZAR TEXTO
    # --------------------------------

    def _normalizar_texto(self, texto):

        if not isinstance(texto, str):
            return ""

        return " ".join(
            texto.lower().strip().split()
        )

    # --------------------------------
    # INTEGRAR CONOCIMIENTO
    # --------------------------------

    def integrar(
        self,
        clave,
        valor,
        fuentes=None
    ):

        if not clave or not valor:
            return None

        # --------------------------------
        # OBTENER CONOCIMIENTO EXISTENTE
        # --------------------------------

        conocimiento_existente = (
            self.conocimiento.obtener(
                clave
            )
        )

        # --------------------------------
        # SI NO EXISTE
        # --------------------------------

        if conocimiento_existente is None:

            self.conocimiento.guardar(
                clave,
                valor,
                "descripcion"
            )

            self._agregar_fuentes(
                clave,
                fuentes
            )

            return "conocimiento_nuevo"

        # --------------------------------
        # NORMALIZAR DATOS
        # --------------------------------

        valor_normalizado = (
            self._normalizar_texto(
                valor
            )
        )

        descripcion = (
            conocimiento_existente.get(
                "descripcion"
            )
        )

        descripcion_normalizada = (
            self._normalizar_texto(
                descripcion
            )
        )

        # --------------------------------
        # YA EXISTE COMO DESCRIPCION
        # --------------------------------

        if (
            valor_normalizado
            == descripcion_normalizada
        ):

            self._agregar_fuentes(
                clave,
                fuentes
            )

            return "dato_ya_existente"

        # --------------------------------
        # OBTENER DATOS ADICIONALES
        # --------------------------------

        datos = conocimiento_existente.get(
            "datos",
            []
        )

        # --------------------------------
        # COMPROBAR SI YA EXISTE
        # --------------------------------

        dato_existente = False

        for dato in datos:

            if (
                self._normalizar_texto(dato)
                == valor_normalizado
            ):

                dato_existente = True

                break

        # --------------------------------
        # AGREGAR NUEVO DATO
        # --------------------------------

        if not dato_existente:

            datos.append(
                valor
            )

            conocimiento_existente[
                "datos"
            ] = datos

        self.conocimiento.actualizar(
            clave,
            conocimiento_existente
        )

        # --------------------------------
        # AGREGAR FUENTES
        # --------------------------------

        self._agregar_fuentes(
            clave,
            fuentes
        )

        if dato_existente:

            return "dato_ya_existente"

        return "dato_integrado"

    # --------------------------------
    # AGREGAR FUENTES
    # --------------------------------

    def _agregar_fuentes(
        self,
        clave,
        fuentes
    ):

        if not fuentes:
            return

        for fuente in fuentes:

            if not fuente:
                continue

            self.conocimiento.agregar_fuente(
                clave,
                fuente.get("tipo"),
                fuente.get("url")
            )
