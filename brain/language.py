# -*- coding: utf-8 -*-

from brain.normalizer import TextNormalizer


class LanguageProcessor:

    def __init__(self, normalizador=None):

        if normalizador is None:
            normalizador = TextNormalizer()

        self.normalizador = normalizador

    def procesar(self, texto):

        texto = self.normalizador.normalizar(
            texto
        )

        if texto == "":
            return {
                "intencion": "vacio",
                "texto": texto
            }

        # -------------------------
        # IDENTIDAD DEL USUARIO
        # -------------------------

        if "cual es mi nombre" in texto:
            return {
                "intencion": "identidad_usuario",
                "clave": "nombre",
                "texto": texto
            }

        # -------------------------
        # IDENTIDAD DE KUKI
        # -------------------------

        if "cual es tu nombre" in texto:
            return {
                "intencion": "identidad_kuki",
                "texto": texto
            }

        # -------------------------
        # SALUDOS
        # -------------------------

        if "hola" in texto or "buenas" in texto:
            return {
                "intencion": "saludo",
                "texto": texto
            }

        # -------------------------
        # ESTADO
        # -------------------------

        if "como estas" in texto:
            return {
                "intencion": "estado",
                "texto": texto
            }

        # -------------------------
        # HORA
        # -------------------------

        if "hora" in texto:
            return {
                "intencion": "hora",
                "texto": texto
            }

        # -------------------------
        # MEMORIA
        # -------------------------

        if "cual es mi " in texto:

            clave = texto.split("cual es mi ", 1)[1]
            clave = clave.strip().rstrip("?")

            return {
                "intencion": "recordar",
                "clave": clave,
                "texto": texto
            }


        # -------------------------
        # BUSQUEDA EN INTERNET
        # -------------------------

        patrones_busqueda = [
            "busca informacion sobre ",
            "busca informacion sobre ",
            "buscar informacion sobre ",
            "buscar informacion sobre ",
            "busca informacion de ",
            "busca informacion de ",
            "buscar informacion de ",
            "buscar informacion de ",
            "consulta informacion sobre ",
            "consulta informacion sobre ",
            "consultar informacion sobre ",
            "consultar informacion sobre ",
            "investiga sobre ",
            "investigar sobre ",
            "busca informacion sobre ",
            "busca informacion sobre ",
            "buscar informacion sobre ",
            "buscar informacion sobre ",
            "busca informacion de ",
            "busca informacion de ",
            "buscar informacion de ",
            "buscar informacion de ",
            "consulta informacion sobre ",
            "consulta informacion sobre ",
            "consultar informacion sobre ",
            "consultar informacion sobre ",
            "investiga sobre ",
            "investigar sobre ",
            "decime informacion sobre ",
            "decime informacion sobre "
        ]

        for patron in patrones_busqueda:

            if texto.startswith(patron):

                consulta = texto[len(patron):].strip()

                if consulta:

                    return {
                        "intencion": "buscar_internet",
                        "consulta": consulta,
                        "texto": texto
                    }

        # -------------------------
        # CONOCIMIENTO
        # -------------------------

        if "que es " in texto:

            clave = texto.split("que es ", 1)[1]
            clave = clave.strip().rstrip("?")

            return {
                "intencion": "conocimiento",
                "clave": clave,
                "categoria": "descripcion",
                "texto": texto
            }

        if "para que sirve " in texto:

            clave = texto.split("para que sirve ", 1)[1]
            clave = clave.strip().rstrip("?")

            return {
                "intencion": "conocimiento",
                "clave": clave,
                "categoria": "usos",
                "texto": texto
            }

        # -------------------------
        # APRENDIZAJE
        # -------------------------

        if texto.startswith("me llamo "):
            return {
                "intencion": "aprendizaje_memoria",
                "texto": texto
            }

        if texto.startswith("mi ") and " es " in texto:
            return {
                "intencion": "aprendizaje_memoria",
                "texto": texto
            }

        if " es " in texto and not texto.startswith("cual es "):
            return {
                "intencion": "aprendizaje_conocimiento",
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
                return {
                    "intencion": "pregunta_contextual",
                    "texto": texto
                }

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
            return {
                "intencion": "consultar_permisos",
                "texto": texto
            }  



        # -------------------------
        # AUTORIZACION DE HERRAMIENTAS
        # -------------------------

        if (
            "autorizo " in texto
            or "permito usar " in texto
            or "permito utilizar " in texto
        ):

            return {
                "intencion": "autorizar_herramienta",
                "texto": texto
            }

        if (
        "revoco " in texto
        or "revocar " in texto
        or "revoca " in texto
        ):

            return {
                "intencion": "revocar_herramienta",
                "texto": texto
            }

        if (
            "rechazo " in texto
            or "deniego " in texto
            or "no permito " in texto
        ):

            return {
                "intencion": "rechazar_herramienta",
                "texto": texto
            }


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
            return {
                "intencion": "usar_herramienta",
                "texto": texto
            }



        # -------------------------
        # DESCONOCIDO
        # -------------------------

        return {
            "intencion": "desconocida",
            "texto": texto
        }