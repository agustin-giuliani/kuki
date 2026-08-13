from brain.response import ResponseGenerator


respuesta = ResponseGenerator()

print("--- GENERADOR DE RESPUESTAS ---")

print(
    respuesta.generar(
        "saludo"
    )
)

print(
    respuesta.generar(
        "identidad_kuki"
    )
)

print(
    respuesta.generar(
        "identidad_usuario",
        {"nombre": "agustin"}
    )
)

print(
    respuesta.generar(
        "recordar",
        {
            "clave": "color favorito",
            "valor": "negro"
        }
    )
)

print(
    respuesta.generar(
        "conocimiento",
        {
            "clave": "python",
            "valor": " un lenguaje de programacion"
        }
    )
)
