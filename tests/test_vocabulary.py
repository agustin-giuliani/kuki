from brain.language.vocabulary import Vocabulary


vocabulario = Vocabulary()


print("--- VOCABULARIO ---")


print(
    "Registrar hola:",
    vocabulario.registrar("hola")
)

print(
    "Registrar Python:",
    vocabulario.registrar("Python")
)

print(
    "Registrar internet:",
    vocabulario.registrar("internet")
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
    ]
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

vocabulario.registrar(
    "hola",
    origen="base"
)

vocabulario.registrar(
    "Python",
    origen="base"
)

vocabulario.registrar(
    "internet",
    origen="herramienta"
)

vocabulario.registrar(
    "blender",
    origen="aprendizaje"
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
