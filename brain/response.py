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

            resultado_tool = datos.get(
                "resultado_tool"
            )

            if resultado_tool is None:
                return "No pude consultar la hora."

            if resultado_tool.get("estado") != "ok":
                return "No pude consultar la hora."

            hora = resultado_tool.get(
                "resultado"
            )

            if hora is None:
                return "No pude obtener la hora."

            return "Son las " + hora

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

            herramienta = datos.get("herramienta")

            if datos.get("permiso_denegado"):

                solicitud = datos.get("solicitud")

                if solicitud:

                    if solicitud["estado"] == "pendiente":

                        return (
                            "Necesito utilizar la herramienta "
                            + herramienta
                            + ", pero no tengo permiso. "
                            "Solicite tu autorizacion."
                        )

                    elif solicitud["estado"] == "ya_pendiente":

                        return (
                            "Ya tengo una solicitud pendiente "
                            "para utilizar "
                            + herramienta
                            + "."
                        )

                return (
                    "Necesito utilizar la herramienta "
                    + herramienta
                    + ", pero no tengo permiso para utilizarla."
                )

            if herramienta:

                return (
                    "La herramienta "
                    + herramienta
                    + " esta disponible."
                )

            return "No pude determinar que herramienta necesito."

        elif intencion == "autorizar_herramienta":

            if datos.get("herramienta_no_encontrada"):

                return "No encuentro esa herramienta."

            herramienta = datos.get("herramienta")
            resultado = datos.get("resultado_autorizacion")

            if resultado is None:

                return "No pude procesar la autorizacion."

            estado = resultado.get("estado")

            if estado == "aprobada":

                return (
                    "Autorizacion concedida. "
                    + herramienta
                    + " ya esta habilitada."
                )

            if estado == "sin_solicitud":

                return (
                    "No existe una solicitud pendiente "
                    "para "
                    + herramienta
                    + "."
                )

            if estado == "error":

                return (
                    "No pude autorizar "
                    + herramienta
                    + "."
                )

            return "No pude procesar la autorizacion."

        elif intencion == "rechazar_herramienta":

            if datos.get("herramienta_no_encontrada"):

                return "No encuentro esa herramienta."

            herramienta = datos.get("herramienta")
            resultado = datos.get("resultado_autorizacion")

            if resultado is None:

                return "No pude procesar el rechazo."

            estado = resultado.get("estado")

            if estado == "rechazada":

                return (
                    "Entendido. No autorizare el uso de "
                    + herramienta
                    + "."
                )

            if estado == "sin_solicitud":

                return (
                    "No existe una solicitud pendiente "
                    "para "
                    + herramienta
                    + "."
                )

            return "No pude procesar el rechazo."

               
        elif intencion == "revocar_herramienta":

            if datos.get("herramienta_no_encontrada"):

                return "No encuentro esa herramienta."

            herramienta = datos.get("herramienta")
            resultado = datos.get("resultado_autorizacion")

            if resultado is None:

                return "No pude procesar la revocacion."

            estado = resultado.get("estado")

            if estado == "revocada":

                return (
                    "Entendido. El permiso de "
                    + herramienta
                    + " fue revocado."
                )

            if estado == "ya_revocada":

                return (
                    "El permiso de "
                    + herramienta
                    + " ya estaba revocado."
                )

            if estado == "permiso_denegado":

                return (
                    "No puedo revocar el permiso de "
                    + herramienta
                    + ". Solo el usuario puede hacerlo."
                )

            return "No pude procesar la revocacion."


        elif intencion == "buscar_internet":

            consulta = datos.get("consulta")

            if datos.get("consulta_invalida"):

                return "No pude determinar que informacion buscar."

            if datos.get("permiso_denegado"):

                solicitud = datos.get("solicitud")

                if solicitud:

                    estado = solicitud.get("estado")

                    if estado == "pendiente":

                        return (
                            "Necesito utilizar Internet para buscar "
                            "informacion sobre "
                            + consulta
                            + ". Solicite tu autorizacion."
                        )

                    elif estado == "ya_pendiente":

                        return (
                            "Ya tengo una solicitud pendiente para "
                            "buscar informacion sobre "
                            + consulta
                            + "."
                        )

                return (
                    "Necesito permiso para buscar informacion "
                    "sobre "
                    + consulta
                    + "."
                )

            resultado_tool = datos.get("resultado_tool")

            if resultado_tool is None:

                return "No pude realizar la busqueda."

            if resultado_tool.get("estado") != "ok":

                return (
                    "No pude buscar informacion sobre "
                    + consulta
                    + "."
                )

            resultado = resultado_tool.get(
                "resultado",
                {}
            )

            resultados = resultado.get(
                "resultados",
                []
            )

            if not resultados:

                return (
                    "No encontre informacion sobre "
                    + consulta
                    + "."
                )

            primero = resultados[0]

            titulo = primero.get(
                "titulo",
                consulta
            )

            descripcion = primero.get(
                "descripcion"
            )

            if descripcion:

                return (
                    "Encontre informacion sobre "
                    + titulo
                    + ". "
                    + descripcion
                    + "."
                )

            return (
                "Encontre informacion sobre "
                + titulo
                + "."
            )


        elif intencion == "consultar_permisos":

            herramientas = datos.get("herramientas")

            if herramientas is None:

                return "No pude consultar mis herramientas."

            if not herramientas:

                return "No tengo herramientas registradas."

            respuesta = (
                "Tengo "
                + str(len(herramientas))
                + " herramientas registradas:"
            )

            for herramienta in herramientas:

                nombre = herramienta["nombre"]
                descripcion = herramienta["descripcion"]
                nivel = herramienta["nivel"]

                permitido = herramienta["permitido"]

                if permitido:
                    estado = "habilitada"
                else:
                    estado = "restringida"

                respuesta += (
                    "\n- "
                    + nombre
                    + ": "
                    + descripcion
                    + " Nivel: "
                    + nivel
                    + ". Estado: "
                    + estado
                    + "."
                )

            return respuesta


        return "No entiendo esa intencion."
