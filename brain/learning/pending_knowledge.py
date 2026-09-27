# -*- coding: utf-8 -*-

import json
import os
from datetime import date


class PendingKnowledge:

    def __init__(
        self,
        archivo="data/pending_knowledge.json"
    ):

        self.archivo = archivo

        # --------------------------------
        # CREAR CARPETA SI NO EXISTE
        # --------------------------------

        carpeta = os.path.dirname(
            self.archivo
        )

        if carpeta:
            os.makedirs(
                carpeta,
                exist_ok=True
            )

        # --------------------------------
        # CREAR ARCHIVO SI NO EXISTE
        # --------------------------------

        if not os.path.exists(
            self.archivo
        ):

            with open(
                self.archivo,
                "w",
                encoding="utf-8"
            ) as archivo:

                json.dump(
                    {},
                    archivo,
                    indent=4,
                    ensure_ascii=False
                )

    # --------------------------------
    # NORMALIZAR CLAVE
    # --------------------------------

    def _normalizar_clave(self, clave):

        if not isinstance(clave, str):
            return ""

        return clave.lower().strip()

    # --------------------------------
    # LEER DATOS
    # --------------------------------

    def _cargar(self):

        with open(
            self.archivo,
            "r",
            encoding="utf-8"
        ) as archivo:

            return json.load(
                archivo
            )

    # --------------------------------
    # GUARDAR DATOS
    # --------------------------------

    def _guardar_archivo(self, datos):

        with open(
            self.archivo,
            "w",
            encoding="utf-8"
        ) as archivo:

            json.dump(
                datos,
                archivo,
                indent=4,
                ensure_ascii=False
            )

    # --------------------------------
    # AGREGAR CONOCIMIENTO PENDIENTE
    # --------------------------------

    def guardar(
        self,
        clave,
        valor,
        tipo_fuente="usuario",
        url=None
    ):

        clave = self._normalizar_clave(
            clave
        )

        if not clave or not valor:
            return None

        conocimiento = self._cargar()

        # --------------------------------
        # CREAR LISTA PARA LA CLAVE
        # --------------------------------

        if clave not in conocimiento:

            conocimiento[clave] = []

        pendientes = conocimiento[clave]

        # --------------------------------
        # BUSCAR SI LA AFIRMACION YA EXISTE
        # --------------------------------

        for pendiente in pendientes:

            if pendiente.get(
                "valor"
            ) == valor:

                # La afirmación ya existe.
                # No creamos otra.
                # Solamente agregamos la fuente.

                self._agregar_fuente(
                    pendiente,
                    tipo_fuente,
                    url
                )

                self._guardar_archivo(
                    conocimiento
                )

                return "pendiente_existente"

        # --------------------------------
        # CREAR NUEVA AFIRMACION
        # --------------------------------

        nueva_fuente = {
            "tipo": tipo_fuente,
            "fecha": str(date.today())
        }

        if url:
            nueva_fuente["url"] = url

        nuevo_pendiente = {
            "valor": valor,
            "fuentes": [
                nueva_fuente
            ]
        }

        pendientes.append(
            nuevo_pendiente
        )

        self._guardar_archivo(
            conocimiento
        )

        return "pendiente_nuevo"

    # --------------------------------
    # AGREGAR FUENTE
    # --------------------------------

    def _agregar_fuente(
        self,
        pendiente,
        tipo_fuente,
        url=None
    ):

        fuentes = pendiente.setdefault(
            "fuentes",
            []
        )

        nueva_fuente = {
            "tipo": tipo_fuente,
            "fecha": str(date.today())
        }

        if url:
            nueva_fuente["url"] = url

        # --------------------------------
        # EVITAR FUENTES DUPLICADAS
        # --------------------------------

        for fuente in fuentes:

            if (
                fuente.get("tipo")
                == tipo_fuente
                and
                fuente.get("url")
                == url
            ):

                return

        fuentes.append(
            nueva_fuente
        )

    # --------------------------------
    # EXISTE LA AFIRMACION
    # --------------------------------

    def existe(
        self,
        clave,
        valor=None
    ):

        clave = self._normalizar_clave(
            clave
        )

        if not clave:
            return False

        conocimiento = self._cargar()

        if clave not in conocimiento:
            return False

        pendientes = conocimiento[clave]

        # --------------------------------
        # EXISTE LA CLAVE
        # --------------------------------

        if valor is None:
            return True

        # --------------------------------
        # EXISTE LA AFIRMACION
        # --------------------------------

        for pendiente in pendientes:

            if pendiente.get(
                "valor"
            ) == valor:

                return True

        return False

    # --------------------------------
    # OBTENER PENDIENTES
    # --------------------------------

    def obtener(self, clave):

        clave = self._normalizar_clave(
            clave
        )

        if not clave:
            return None

        conocimiento = self._cargar()

        if clave not in conocimiento:
            return None

        return conocimiento[clave]

    # --------------------------------
    # ELIMINAR AFIRMACION
    # --------------------------------

    def eliminar(
        self,
        clave,
        valor
    ):

        clave = self._normalizar_clave(
            clave
        )

        if not clave:
            return False

        conocimiento = self._cargar()

        if clave not in conocimiento:
            return False

        pendientes = conocimiento[clave]

        nuevos_pendientes = []

        eliminada = False

        for pendiente in pendientes:

            if pendiente.get(
                "valor"
            ) == valor:

                eliminada = True

                continue

            nuevos_pendientes.append(
                pendiente
            )

        # --------------------------------
        # SI NO EXISTIA
        # --------------------------------

        if not eliminada:
            return False

        # --------------------------------
        # ACTUALIZAR AFIRMACIONES
        # --------------------------------

        if nuevos_pendientes:

            conocimiento[clave] = (
                nuevos_pendientes
            )

        else:

            # Si ya no quedan afirmaciones
            # pendientes para esa clave,
            # eliminamos la clave completa.

            del conocimiento[clave]

        self._guardar_archivo(
            conocimiento
        )

        return True
