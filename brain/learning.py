from brain.knowledge import Knowledge


class Learning:

    def __init__(self, memoria, conocimiento):
        self.memoria = memoria
        self.conocimiento = conocimiento

    def aprender_frase(self, texto):

        texto = texto.lower().strip()

        # No aprender preguntas
        if texto.startswith("que es "):
            return None

        if texto.startswith("cual es "):
            return None

        # Aprender nombre
        if texto.startswith("me llamo "):

            nombre = texto[9:].strip()

            if nombre:
                self.memoria.guardar("nombre", nombre)
                return "memoria"

        if " es " not in texto:
            return None

        clave, valor = texto.split(" es ", 1)

        clave = clave.strip()
        valor = valor.strip().rstrip(".")

        if not clave or not valor:
            return None

        # Informacion personal
        if texto.startswith("mi "):

            clave = clave[3:].strip()

            if clave.startswith("cual"):
                return None

            self.memoria.guardar(clave, valor)

            return "memoria"

        # Conocimiento general
        self.conocimiento.guardar(
            clave,
            valor,
            "descripcion"
        )

        return "conocimiento"