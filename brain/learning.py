class Learning:

    def __init__(self, memoria):
        self.memoria = memoria

    def aprender_frase(self, texto):

        texto = texto.lower().strip()

        if not texto.startswith("mi "):
            return False

        if " es " not in texto:
            return False

        contenido = texto[3:]

        clave, valor = contenido.split(" es ", 1)

        clave = clave.strip()
        valor = valor.strip().rstrip(".")

        if not clave or not valor:
            return False

        # Evitamos guardar preguntas como si fueran conocimientos
        if clave.startswith("cual"):
            return False

        self.memoria.guardar(clave, valor)

        return True
