class LanguageProcessor:

    def procesar(self, texto):

        texto = texto.lower().strip()

        if texto == "":
            return {
                "intencion": "vacio",
                "texto": ""
            }

        if "hola" in texto or "buenas" in texto:
            return {
                "intencion": "saludo",
                "texto": texto
            }

        if "como estas" in texto:
            return {
                "intencion": "estado",
                "texto": texto
            }

        if "nombre" in texto:
            return {
                "intencion": "nombre",
                "texto": texto
            }

        
        if "hora" in texto:
            return {
                "intencion": "hora",
                "texto": texto
            }

        
        # Preguntas para recuperar informacion de la memoria
        if "cual es mi " in texto:
            clave = texto.split("cual es mi ", 1)[1]
            clave = clave.strip().rstrip("?")

            return {
                "intencion": "recordar",
                "clave": clave,
                "texto": texto
            }

        return {
            "intencion": "desconocida",
            "texto": texto
        }
