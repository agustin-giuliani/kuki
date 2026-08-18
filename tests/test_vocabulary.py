from brain.language.vocabulary import Vocabulary


vocabulario = Vocabulary()


print("--- VOCABULARIO ---")


print(
    "Registrar hola:",
    vocabulario.registrar(
        "hola",
        origen="base"
    )
)

print(
    "Registrar Python:",
    vocabulario.registrar(
        "Python",
        origen="base"
    )
)

print(
    "Registrar internet:",
    vocabulario.registrar(
        "internet",
        origen="herramienta"
    )
)


print()
print("Conoce hola:")
print(
    vocabulario.conoce("hola")
)


print()
print("Conoce python:")
print(
    vocabulario.conoce("python")
)


print()
print("Conoce blender:")
print(
    vocabulario.conoce("blender")
)


print()
print("Registrar muchas:")

cantidad = vocabulario.registrar_muchas(
    [
        "hora",
        "herramienta",
        "memoria",
        "conocimiento"
    ],
    origen="base"
)

print(cantidad)


print()
print("Cantidad:")
print(
    vocabulario.cantidad()
)


print()
print("Palabras:")

print(
    vocabulario.listar()
)


print()
print("Eliminar internet:")

print(
    vocabulario.eliminar("internet")
)


print()
print("Conoce internet:")

print(
    vocabulario.conoce("internet")
)


print()
print("Registrar blender:")

print(
    vocabulario.registrar(
        "blender",
        origen="aprendizaje"
    )
)


print()
print("Origen de hola:")
print(
    vocabulario.origen("hola")
)


print()
print("Origen de python:")
print(
    vocabulario.origen("python")
)


print()
print("Origen de blender:")
print(
    vocabulario.origen("blender")
)


print()
print("Palabras de origen base:")
print(
    vocabulario.listar_por_origen("base")
)


print()
print("Palabras de origen aprendizaje:")
print(
    vocabulario.listar_por_origen("aprendizaje")
)


print()
print("Palabras de origen herramienta:")
print(
    vocabulario.listar_por_origen("herramienta")
)


print()
print("DUPLICADOS:")

print(
    "Registrar blender nuevamente:",
    vocabulario.registrar(
        "blender",
        origen="herramienta"
    )
)

print(
    "Conoce blender:",
    vocabulario.conoce("blender")
)

print(
    "Origen de blender:",
    vocabulario.origen("blender")
)


print()
print("MAYUSCULAS:")

print(
    "Registrar PYTHON:",
    vocabulario.registrar(
        "PYTHON",
        origen="aprendizaje"
    )
)

print(
    "Conoce python:",
    vocabulario.conoce("python")
)

print(
    "Origen de python:",
    vocabulario.origen("python")
)