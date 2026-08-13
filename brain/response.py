class ResponseGenerator:

    def generar(self, intencion, datos=None):

        if datos is None:
            datos = {}

        if intencion == "saludo":
            return "Hola Agustin. Como estas?"

        elif intencion == "estado":
            return "Estoy funcionando correctamente."

        elif intencion == "identidad_kuki":
            return "Mi nombre es KUKI."

        if intencion == "hora":

            if datos.get("permiso_denegado"):
                return "No tengo permiso para consultar la hora."

            return "Son las " + datos["hora"]

        elif intencion == "identidad_usuario":

            nombre = datos.get("nombre")

            if nombre:
                return "Tu nombre es " + nombre + "."

            return "Todavia no se tu nombre."

        elif intencion == "recordar":

            clave = datos.get("clave")
            valor = datos.get("valor")

            if valor is not None:
                return "Tu " + clave + " es " + valor + "."

            return "No recuerdo eso todavia."

        elif intencion == "conocimiento":

            clave = datos.get("clave")
            categoria = datos.get("categoria", "descripcion")
            valor = datos.get("valor")

            if valor is None:
                return "Todavia no conozco eso."

            if categoria == "descripcion":
                return clave.capitalize() + " es " + valor + "."

            elif categoria == "usos":
                return (
                    clave.capitalize()
                    + " sirve para "
                    + valor
                    + "."
                )

            return clave.capitalize() + ": " + valor + "."

        elif intencion == "desconocida":
            return "Todavia no se como responder a eso."

        elif intencion == "pregunta_contextual":

            tema = datos.get("tema")
            valor = datos.get("valor")

            if tema is None:
                return "No tengo un tema anterior para relacionar con tu pregunta."

            if valor is None:
                return (
                    "Entiendo que estas preguntando sobre "
                    + tema
                    + ", pero todavia no tengo suficiente informacion."
                )

            return (
                tema.capitalize()
                + " sirve para "
                + valor
                + "."
            )

        elif intencion == "usar_herramienta":

            if datos.get("herramienta_no_encontrada"):

                return "No encuentro una herramienta adecuada para eso."

            if datos.get("permiso_denegado"):

                herramienta = datos.get("herramienta")

                if herramienta:

                    return (
                        "Necesito utilizar la herramienta "
                        + herramienta
                        + ", pero no tengo permiso para utilizarla."
                    )

                return "No tengo permiso para utilizar esa herramienta."

            herramienta = datos.get("herramienta")

            if herramienta:

                return (
                    "La herramienta "
                    + herramienta
                    + " esta disponible."
                )

            return "No pude determinar que herramienta necesito."

        return "No entiendo esa intencion."
