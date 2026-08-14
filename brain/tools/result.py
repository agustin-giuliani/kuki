class ToolResult:

    def __init__(
        self,
        estado,
        resultado=None,
        mensaje=None,
        herramienta=None
    ):

        self.estado = estado
        self.resultado = resultado
        self.mensaje = mensaje
        self.herramienta = herramienta

    def to_dict(self):

        datos = {
            "estado": self.estado,
            "resultado": self.resultado,
            "mensaje": self.mensaje,
            "herramienta": self.herramienta
        }

        return datos
