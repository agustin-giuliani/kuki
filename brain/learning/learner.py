# -*- coding: utf-8 -*-

from brain.learning.knowledge_integrator import KnowledgeIntegrator


class Learning:

    def __init__(
        self,
        memoria,
        conocimiento,
        pending_knowledge,
        knowledge_integrator,
        memory_integrator
    ):

        # --------------------------------
        # COMPONENTES DE APRENDIZAJE
        # --------------------------------

        # Memory se encarga del almacenamiento
        # físico de los recuerdos.
        self.memoria = memoria

        # Knowledge se encarga del almacenamiento
        # del conocimiento general.
        self.conocimiento = conocimiento

        # PendingKnowledge guarda información externa
        # que todavía no fue validada.
        self.pending_knowledge = pending_knowledge

        # KnowledgeIntegrator decide cómo integrar
        # nueva información al conocimiento existente.
        self.knowledge_integrator = knowledge_integrator

        # MemoryIntegrator decide cómo organizar
        # la información personal antes de guardarla.
        self.memory_integrator = memory_integrator

    # --------------------------------
    # APRENDER
    # --------------------------------

    def aprender(self, resultado):

        # Si no recibimos ningún resultado,
        # no hay nada que aprender.
        if not resultado:
            return None

        # Obtenemos la intención detectada
        # por LanguageProcessor.
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

        # Si la intención no corresponde
        # a ningún aprendizaje conocido,
        # no hacemos nada.
        return None

    # --------------------------------
    # APRENDER MEMORIA
    # --------------------------------

    def _aprender_memoria(self, resultado):

        # Obtenemos la clave del recuerdo.
        #
        # Ejemplo:
        #
        # "color favorito"
        #
        clave = resultado.get(
            "clave"
        )

        # Obtenemos el valor que queremos recordar.
        #
        # Ejemplo:
        #
        # "negro"
        #
        valor = resultado.get(
            "valor"
        )

        # Si falta alguno de los datos,
        # no podemos crear el recuerdo.
        if not clave or not valor:
            return None

        # --------------------------------
        # DETERMINAR TIPO DE MEMORIA
        # --------------------------------

        # Por ahora utilizamos el tipo que venga
        # desde el resultado del procesamiento
        # del lenguaje.
        #
        # Si todavía no existe, utilizamos
        # "dato_unico" como comportamiento
        # predeterminado.
        tipo = resultado.get(
            "tipo_memoria",
            "dato_unico"
        )

        # --------------------------------
        # DETERMINAR CATEGORIA
        # --------------------------------

        # Obtenemos la categoría de la memoria.
        #
        # Si todavía no viene determinada,
        # utilizamos "general".
        categoria = resultado.get(
            "categoria_memoria",
            "general"
        )

        # --------------------------------
        # INTEGRAR MEMORIA
        # --------------------------------

        # Learning no guarda directamente
        # el dato en Memory.
        #
        # Delegamos esa responsabilidad
        # al MemoryIntegrator.
        return self.memory_integrator.integrar(
            clave,
            valor,
            tipo,
            categoria
        )

    # --------------------------------
    # APRENDER CONOCIMIENTO
    # --------------------------------

    def _aprender_conocimiento(self, resultado):

        # Obtenemos la clave del conocimiento.
        clave = resultado.get(
            "clave"
        )

        # Obtenemos el valor del conocimiento.
        valor = resultado.get(
            "valor"
        )

        # Si falta alguno de los datos,
        # no podemos aprenderlo.
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

        # Validamos que tengamos los datos
        # necesarios para realizar la evaluación.
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

        # Si no existe ningún conocimiento
        # relacionado con esta clave,
        # se considera conocimiento nuevo.
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

        # Si la información nueva es exactamente
        # igual a la descripción existente,
        # no necesitamos modificarla.
        if descripcion_existente == valor:

            return "conocimiento_igual"

        # --------------------------------
        # INFORMACION DIFERENTE
        # --------------------------------

        # La clave existe, pero recibimos
        # información diferente.
        return "conocimiento_nuevo_dato"

    # --------------------------------
    # APRENDER DESDE UNA FRASE
    # --------------------------------

    def aprender_frase(self, texto):

        # Normalizamos el texto recibido.
        texto = texto.lower().strip()

        # --------------------------------
        # NO APRENDER PREGUNTAS
        # --------------------------------

        # Una pregunta como:
        #
        # "¿Qué es Python?"
        #
        # no debe convertirse automáticamente
        # en conocimiento.
        if texto.startswith("que es "):
            return None

        if texto.startswith("cual es "):
            return None

        # --------------------------------
        # APRENDER NOMBRE
        # --------------------------------

        if texto.startswith("me llamo "):

            # Extraemos el nombre.
            nombre = texto[9:].strip()

            if nombre:

                # Utilizamos el MemoryIntegrator
                # en lugar de guardar directamente.
                return self.memory_integrator.integrar(
                    "nombre",
                    nombre,
                    "dato_unico",
                    "identidad"
                )

        # --------------------------------
        # FRASE DE CONOCIMIENTO
        # --------------------------------

        if " es " not in texto:
            return None

        # Separamos la clave del valor.
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

            # Quitamos "mi" de la clave.
            #
            # "mi color favorito"
            #
            # pasa a ser:
            #
            # "color favorito"
            clave = clave[3:].strip()

            if clave.startswith("cual"):
                return None

            # Por ahora tratamos los datos personales
            # detectados mediante "mi ..." como
            # datos únicos de categoría preferencia.
            return self.memory_integrator.integrar(
                clave,
                valor,
                "dato_unico",
                "preferencia"
            )

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

    def recordar_memoria(
        self,
        clave,
        campo=None
    ):

        # --------------------------------
        # OBTENER MEMORIA
        # --------------------------------

        # Pedimos a Memory la información almacenada.
        #
        # Memory solamente se encarga de recuperar
        # lo que existe en el archivo.
        memoria = self.memoria.recordar(
            clave
        )

        # Si no existe ningún recuerdo con esa clave,
        # devolvemos None.
        if memoria is None:
            return None

        # --------------------------------
        # COMPATIBILIDAD CON MEMORIA ANTIGUA
        # --------------------------------

        # Las memorias antiguas podían estar guardadas
        # directamente como texto.
        #
        # Ejemplo:
        #
        # "nombre": "agustin"
        #
        # En ese caso devolvemos directamente
        # ese valor.
        if isinstance(
            memoria,
            str
        ):

            return memoria

        # --------------------------------
        # MEMORIA ESTRUCTURADA
        # --------------------------------

        # Si se solicita un campo concreto,
        # intentamos devolver solamente ese campo.
        #
        # Ejemplo:
        #
        # recordar_memoria(
        #     "nombre",
        #     "valor"
        # )
        #
        # devuelve:
        #
        # "agustin"
        if campo:

            return memoria.get(
                campo
            )

        # --------------------------------
        # DATO UNICO
        # --------------------------------

        # Si la memoria es un dato único,
        # normalmente queremos devolver su "valor".
        #
        # Ejemplo:
        #
        # {
        #     "valor": "negro",
        #     "categoria": "preferencia",
        #     "tipo": "dato_unico"
        # }
        #
        # devuelve:
        #
        # "negro"
        if memoria.get(
            "tipo"
        ) == "dato_unico":

            return memoria.get(
                "valor"
            )

        # --------------------------------
        # LISTA
        # --------------------------------

        # Si la memoria representa una lista,
        # devolvemos todos sus valores.
        #
        # Ejemplo:
        #
        # {
        #     "valores": [
        #         "cordoba",
        #         "mendoza"
        #     ],
        #     "tipo": "lista"
        # }
        #
        # devuelve:
        #
        # [
        #     "cordoba",
        #     "mendoza"
        # ]
        if memoria.get(
            "tipo"
        ) == "lista":

            return memoria.get(
                "valores",
                []
            )

        # --------------------------------
        # FORMATO DESCONOCIDO
        # --------------------------------

        # Si en el futuro agregamos nuevos tipos
        # de memoria y todavía no definimos
        # cómo devolverlos, mantenemos disponible
        # la estructura completa.
        return memoria
        # --------------------------------
        # RECORDAR CONOCIMIENTO
        # --------------------------------

    def recordar_conocimiento(
        self,
        clave,
        categoria="descripcion"
    ):

        # Knowledge recupera la categoría
        # solicitada del conocimiento.
        return self.conocimiento.recordar(
            clave,
            categoria
        )

    # --------------------------------
    # APRENDIZAJE EXTERNO
    # --------------------------------

    def aprender_externo(self, resultado_tool):

        # Si no recibimos ningún resultado,
        # no podemos aprender nada.
        if not resultado_tool:
            return None

        # Solo procesamos herramientas
        # que hayan terminado correctamente.
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

        # Por ahora utilizamos el primer resultado.
        primer_resultado = resultados[0]

        if not primer_resultado:
            return None

        # Extraemos la información obtenida.
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

        # --------------------------------
        # EVALUAR CONOCIMIENTO EXISTENTE
        # --------------------------------

        evaluacion = self._evaluar_conocimiento(
            clave,
            descripcion
        )

        # --------------------------------
        # CONOCIMIENTO YA CONOCIDO
        # --------------------------------

        if evaluacion == "conocimiento_igual":

            return "conocimiento_igual"

        # --------------------------------
        # INFORMACION NUEVA O DIFERENTE
        # --------------------------------

        # La información externa todavía no pasa
        # directamente a Knowledge.
        #
        # Primero queda pendiente de validación.
        self.pending_knowledge.guardar(
            clave,
            descripcion,
            "internet",
            url
        )

        return "pendiente"

    # --------------------------------
    # VALIDAR CONOCIMIENTO PENDIENTE
    # --------------------------------

    def validar_conocimiento(
        self,
        clave,
        valor
    ):

        # --------------------------------
        # OBTENER INFORMACION PENDIENTE
        # --------------------------------

        pendientes = self.pending_knowledge.obtener(
            clave
        )

        if not pendientes:
            return None

        # --------------------------------
        # BUSCAR LA AFIRMACION
        # --------------------------------

        pendiente_encontrado = None

        for pendiente in pendientes:

            if pendiente.get(
                "valor"
            ) == valor:

                pendiente_encontrado = pendiente

                break

        if pendiente_encontrado is None:
            return None

        # --------------------------------
        # OBTENER FUENTES
        # --------------------------------

        fuentes = pendiente_encontrado.get(
            "fuentes",
            []
        )

        # --------------------------------
        # INTEGRAR EN KNOWLEDGE
        # --------------------------------

        resultado = self.knowledge_integrator.integrar(
            clave,
            valor,
            fuentes
        )

        # --------------------------------
        # SI LA INTEGRACION FALLO
        # --------------------------------

        if resultado is None:
            return None

        # --------------------------------
        # ELIMINAR DE PENDING
        # --------------------------------

        eliminado = self.pending_knowledge.eliminar(
            clave,
            valor
        )

        if not eliminado:
            return None

        return "conocimiento_validado"