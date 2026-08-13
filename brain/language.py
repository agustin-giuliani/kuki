class LanguageProcessor:

    def procesar(self, texto):

        texto = texto.lower().strip()

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