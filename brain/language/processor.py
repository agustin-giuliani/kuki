# -*- coding: utf-8 -*-

from brain.language.normalizer import TextNormalizer
from brain.language.spell_corrector import SpellCorrector
from brain.language.variant_detector import VariantDetector


class LanguageProcessor:

    def __init__(
        self,
        normalizador=None,
        corrector=None,
        detector_variantes=None
    ):

        if normalizador is None:
            normalizador = TextNormalizer()

        if corrector is None:
            corrector = SpellCorrector()

        if detector_variantes is None:
            detector_variantes = VariantDetector(
                corrector.vocabulario
            )

        self.normalizador = normalizador
        self.corrector = corrector
        self.detector_variantes = detector_variantes

    # --------------------------------
    # CREAR RESULTADO
    # --------------------------------

    def crear_resultado(
        self,
        intencion,
        texto,
        variantes=None,
        **datos
    ):

        resultado = {
            "intencion": intencion,
            "texto": texto
        }

        if variantes:
            resultado["variantes"] = variantes

        resultado.update(datos)

        return resultado

    # --------------------------------
    # PROCESAR TEXTO
    # --------------------------------

    def procesar(self, texto):

        # -------------------------
        # NORMALIZACION
        # -------------------------

        texto = self.normalizador.normalizar(
            texto
        )

        texto_original = texto

        # -------------------------
        # CORRECCION
        # -------------------------

        texto = self.corrector.corregir(
            texto
        )

        # -------------------------
        # DETECCION DE VARIANTES
        # -------------------------

        analisis_variantes = []

        for palabra in texto_original.split():

            analisis = self.detector_variantes.detectar(
                palabra
            )

            if analisis["estado"] not in (
                "conocida",
                "sin_variante"
            ):

                analisis_variantes.append(
                    analisis
                )

        # -------------------------
        # TEXTO VACIO
        # -------------------------

        if texto == "":
            return self.crear_resultado(
                "vacio",
                texto,
                analisis_variantes
            )

        # -------------------------
        # IDENTIDAD DEL USUARIO
        # -------------------------

        if "cual es mi nombre" in texto:

            return self.crear_resultado(
                "identidad_usuario",
                texto,
                analisis_variantes,
                clave="nombre"
            )

        # -------------------------
        # IDENTIDAD DE KUKI
        # -------------------------

        if "cual es tu nombre" in texto:

            return self.crear_resultado(
                "identidad_kuki",
                texto,
                analisis_variantes
            )

        # -------------------------
        # SALUDOS
        # -------------------------

        if "hola" in texto or "buenas" in texto:

            return self.crear_resultado(
                "saludo",
                texto,
                analisis_variantes
            )

        # -------------------------
        # ESTADO
        # -------------------------

        if "como estas" in texto:

            return self.crear_resultado(
                "estado",
                texto,
                analisis_variantes
            )

        # -------------------------
        # HORA
        # -------------------------

        if "hora" in texto:

            return self.crear_resultado(
                "hora",
                texto,
                analisis_variantes
            )

        # -------------------------
        # MEMORIA
        # -------------------------

        if "cual es mi " in texto:

            clave = texto.split(
                "cual es mi ",
                1
            )[1]

            clave = clave.strip().rstrip("?")

            return self.crear_resultado(
                "recordar",
                texto,
                analisis_variantes,
                clave=clave
            )

        # -------------------------
        # BUSQUEDA EN INTERNET
        # -------------------------

        patrones_busqueda = [
            "busca informacion sobre ",
            "buscar informacion sobre ",
            "busca informacion de ",
            "buscar informacion de ",
            "consulta informacion sobre ",
            "consultar informacion sobre ",
            "investiga sobre ",
            "investigar sobre ",
            "decime informacion sobre "
        ]

        for patron in patrones_busqueda:

            if texto.startswith(patron):

                consulta = texto[
                    len(patron):
                ].strip()

                if consulta:

                    return self.crear_resultado(
                        "buscar_internet",
                        texto,
                        analisis_variantes,
                        consulta=consulta
                    )

        # -------------------------
        # CONOCIMIENTO
        # -------------------------

        if "que es " in texto:

            clave = texto.split(
                "que es ",
                1
            )[1]

            clave = clave.strip().rstrip("?")

            return self.crear_resultado(
                "conocimiento",
                texto,
                analisis_variantes,
                clave=clave,
                categoria="descripcion"
            )

        if "para que sirve " in texto:

            clave = texto.split(
                "para que sirve ",
                1
            )[1]

            clave = clave.strip().rstrip("?")

            return self.crear_resultado(
                "conocimiento",
                texto,
                analisis_variantes,
                clave=clave,
                categoria="usos"
            )

        # -------------------------
        # APRENDIZAJE
        # -------------------------

        if texto.startswith("me llamo "):

            nombre = texto[9:].strip()

            if nombre:

                return {
                    "intencion": "aprendizaje_memoria",
                    "tipo": "nombre",
                    "clave": "nombre",
                    "valor": nombre,
                    "texto": texto
                }


        if texto.startswith("mi ") and " es " in texto:

            clave, valor = texto.split(
                " es ",
                1
            )

            clave = clave[3:].strip()
            valor = valor.strip().rstrip(".")

            if clave and valor:

                return {
                    "intencion": "aprendizaje_memoria",
                    "tipo": "dato_usuario",
                    "clave": clave,
                    "valor": valor,
                    "texto": texto
                }


        if " es " in texto and not texto.startswith("cual es "):

            clave, valor = texto.split(
                " es ",
                1
            )

            clave = clave.strip()
            valor = valor.strip().rstrip(".")

            if clave and valor:

                return {
                    "intencion": "aprendizaje_conocimiento",
                    "tipo": "conocimiento",
                    "clave": clave,
                    "valor": valor,
                    "texto": texto
                }

        # -------------------------
        # PREGUNTA CONTEXTUAL
        # -------------------------

        if (
            "para que sirve" in texto
            or "para que se usa" in texto
            or "como funciona" in texto
            or "y que hace" in texto
        ):

            return self.crear_resultado(
                "pregunta_contextual",
                texto,
                analisis_variantes
            )

        # -------------------------
        # CONSULTA DE PERMISOS
        # -------------------------

        if (
            "que herramientas tenes" in texto
            or "que herramientas tienes" in texto
            or "que herramientas estan habilitadas" in texto
            or "que permisos tenes" in texto
            or "cuales son tus permisos" in texto
        ):

            return self.crear_resultado(
                "consultar_permisos",
                texto,
                analisis_variantes
            )

        # -------------------------
        # AUTORIZACION
        # -------------------------

        if (
            "autorizo " in texto
            or "permito usar " in texto
            or "permito utilizar " in texto
        ):

            return self.crear_resultado(
                "autorizar_herramienta",
                texto,
                analisis_variantes
            )

        # -------------------------
        # REVOCACION
        # -------------------------

        if (
            "revoco " in texto
            or "revocar " in texto
            or "revoca " in texto
        ):

            return self.crear_resultado(
                "revocar_herramienta",
                texto,
                analisis_variantes
            )

        # -------------------------
        # RECHAZO
        # -------------------------

        if (
            "rechazo " in texto
            or "deniego " in texto
            or "no permito " in texto
        ):

            return self.crear_resultado(
                "rechazar_herramienta",
                texto,
                analisis_variantes
            )

        # -------------------------
        # USO DE HERRAMIENTAS
        # -------------------------

        if (
            "quiero consultar internet" in texto
            or "necesito internet" in texto
            or "usa internet" in texto
            or "usar internet" in texto
            or "busca en internet" in texto
            or "consultar internet" in texto
            or "consulta internet" in texto
        ):

            return self.crear_resultado(
                "usar_herramienta",
                texto,
                analisis_variantes
            )

        # -------------------------
        # DESCONOCIDO
        # -------------------------

        return self.crear_resultado(
            "desconocida",
            texto,
            analisis_variantes
        )