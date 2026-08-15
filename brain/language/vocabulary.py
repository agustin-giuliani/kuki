# -*- coding: utf-8 -*-


class Vocabulary:

    def __init__(self):

        self.palabras = set()

    def registrar(self, palabra):

        palabra = palabra.lower().strip()

        if not palabra:
            return False

        self.palabras.add(palabra)

        return True

    def registrar_muchas(self, palabras):

        cantidad = 0

        for palabra in palabras:

            if self.registrar(palabra):
                cantidad += 1

        return cantidad

    def conoce(self, palabra):

        palabra = palabra.lower().strip()

        return palabra in self.palabras

    def eliminar(self, palabra):

        palabra = palabra.lower().strip()

        if palabra not in self.palabras:
            return False

        self.palabras.remove(palabra)

        return True

    def listar(self):

        return sorted(
            self.palabras
        )

    def cantidad(self):

        return len(self.palabras)
