class ToolSelector:

    def __init__(self, catalogo):
        self.catalogo = catalogo

    def seleccionar(self, texto):

        texto = texto.lower().strip()

        if not texto:
            return None

        herramientas = self.catalogo.listar()

        mejor_herramienta = None
        mejor_puntuacion = 0

        palabras = set(texto.split())

        for herramienta in herramientas:

            contenido = (
                herramienta["nombre"]
                + " "
                + herramienta["descripcion"]
            ).lower()

            palabras_herramienta = set(
                contenido.split()
            )

            coincidencias = palabras.intersection(
                palabras_herramienta
            )

            puntuacion = len(coincidencias)

            # Exigimos al menos una coincidencia
            if puntuacion >= 1:

                if puntuacion > mejor_puntuacion:

                    mejor_puntuacion = puntuacion
                    mejor_herramienta = herramienta["nombre"]

        return mejor_herramienta
