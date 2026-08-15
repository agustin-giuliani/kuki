# -*- coding: utf-8 -*-


class Vocabulary:

    def __init__(self):

        self.palabras = {}

    def registrar(
        self,
        palabra,
        origen="desconocido"
    ):

        palabra = palabra.lower().strip()

        if not palabra:
            return False

        self.palabras[palabra] = origen

        return True

    def registrar_muchas(
        self,
        palabras,
        origen="desconocido"
    ):

        cantidad = 0

        for palabra in palabras:

            if self.registrar(
                palabra,
                origen
            ):
                cantidad += 1

        return cantidad

    def conoce(self, palabra):

        palabra = palabra.lower().strip()

        return palabra in self.palabras

    def origen(self, palabra):

        palabra = palabra.lower().strip()

        return self.palabras.get(
            palabra
        )

    def eliminar(self, palabra):

        palabra = palabra.lower().strip()

        if palabra not in self.palabras:
            return False

        del self.palabras[palabra]

        return True

    def listar(self):

        return sorted(
            self.palabras.keys()
        )

    def listar_por_origen(self, origen):

        palabras = []

        for palabra, origen_palabra in self.palabras.items():

            if origen_palabra == origen:
                palabras.append(palabra)

        return sorted(palabras)

    def cantidad(self):

        return len(self.palabras)