# -*- coding: utf-8 -*-


class MemoryIntegrator:

    def __init__(self, memoria):

        # Guardamos una referencia al objeto Memory.
        #
        # Memory se encarga de guardar y recuperar información.
        # MemoryIntegrator se encarga de decidir cómo
        # organizar esa información.
        self.memoria = memoria

    # --------------------------------
    # NORMALIZAR CLAVE
    # --------------------------------

    def _normalizar_clave(self, clave):

        # Comprobamos que la clave sea un texto.
        if not isinstance(clave, str):
            return ""

        # Eliminamos espacios innecesarios
        # y convertimos la clave a minúsculas.
        return clave.strip().lower()

    # --------------------------------
    # NORMALIZAR VALOR
    # --------------------------------

    def _normalizar_valor(self, valor):

        # Comprobamos que el valor sea un texto.
        if not isinstance(valor, str):
            return ""

        # Eliminamos espacios al principio y al final.
        return valor.strip()

    # --------------------------------
    # INTEGRAR MEMORIA
    # --------------------------------

    def integrar(
        self,
        clave,
        valor,
        tipo="dato_unico",
        categoria="general"
    ):

        # --------------------------------
        # NORMALIZAR DATOS
        # --------------------------------

        clave = self._normalizar_clave(
            clave
        )

        valor = self._normalizar_valor(
            valor
        )

        # Si falta la clave o el valor,
        # no podemos guardar la memoria.
        if not clave or not valor:
            return None

        # --------------------------------
        # OBTENER MEMORIA EXISTENTE
        # --------------------------------

        memoria_existente = self.memoria.recordar(
            clave
        )

        # --------------------------------
        # DATO UNICO
        # --------------------------------

        if tipo == "dato_unico":

            # Un dato único representa información
            # que tiene un único valor actual.
            #
            # Ejemplo:
            #
            # color_favorito -> negro
            #
            # Si posteriormente llega:
            #
            # color_favorito -> azul
            #
            # se reemplaza el valor anterior.

            datos = {
                "valor": valor,
                "categoria": categoria,
                "tipo": "dato_unico"
            }

            self.memoria.guardar(
                clave,
                datos
            )

            return "memoria_integrada"

        # --------------------------------
        # LISTA
        # --------------------------------

        if tipo == "lista":

            # --------------------------------
            # MEMORIA NUEVA
            # --------------------------------

            # Si no existe ninguna memoria para esta clave,
            # creamos una lista nueva.
            if memoria_existente is None:

                datos = {
                    "valores": [
                        valor
                    ],
                    "categoria": categoria,
                    "tipo": "lista"
                }

                self.memoria.guardar(
                    clave,
                    datos
                )

                return "memoria_integrada"

            # --------------------------------
            # COMPATIBILIDAD CON MEMORIA VIEJA
            # --------------------------------

            # Puede existir información guardada
            # con el formato antiguo.
            #
            # Ejemplo:
            #
            # "lugares_favoritos": "cordoba"
            #
            # En ese caso, memoria_existente será un string
            # y no podremos utilizar .get().
            #
            # Convertimos ese dato antiguo al nuevo formato.

            if isinstance(
                memoria_existente,
                str
            ):

                valores = [
                    memoria_existente
                ]

                # Si el nuevo valor todavía no existe,
                # lo agregamos a la lista.
                if valor not in valores:

                    valores.append(
                        valor
                    )

                datos = {
                    "valores": valores,
                    "categoria": categoria,
                    "tipo": "lista"
                }

                self.memoria.guardar(
                    clave,
                    datos
                )

                return "memoria_integrada"

            # --------------------------------
            # OBTENER LISTA EXISTENTE
            # --------------------------------

            # Intentamos recuperar la lista existente.
            valores = memoria_existente.get(
                "valores",
                []
            )

            # --------------------------------
            # EVITAR DUPLICADOS
            # --------------------------------

            # Si el valor ya existe,
            # no lo agregamos nuevamente.
            if valor in valores:

                return "memoria_ya_existente"

            # --------------------------------
            # AGREGAR NUEVO VALOR
            # --------------------------------

            valores.append(
                valor
            )

            # Actualizamos la lista.
            memoria_existente[
                "valores"
            ] = valores

            # Guardamos nuevamente la memoria.
            self.memoria.guardar(
                clave,
                memoria_existente
            )

            return "memoria_integrada"

        # --------------------------------
        # TIPO NO SOPORTADO
        # --------------------------------

        # Si recibimos un tipo que todavía
        # no conocemos, no hacemos nada.
        return None