class ToolRegistry:

    def __init__(self):
        self.herramientas = {}

    def registrar(
        self,
        nombre,
        funcion,
        descripcion="",
        capacidades=None
    ):

        if capacidades is None:
            capacidades = []

        self.herramientas[nombre] = {
            "funcion": funcion,
            "descripcion": descripcion,
            "capacidades": capacidades
        }

    def existe(self, nombre):

        return nombre in self.herramientas

    def obtener(self, nombre):

        return self.herramientas.get(nombre)

    def listar(self):

        return list(self.herramientas.keys())