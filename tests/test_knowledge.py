from brain.learning.knowledge import Knowledge


knowledge = Knowledge()

print("--- KNOWLEDGE DE KUKI ---")


print(
    "Descripcion:",
    knowledge.recordar("python")
)


knowledge.guardar(
    "python",
    "desarrollar aplicaciones, automatizar tareas y analizar datos",
    "usos"
)


print(
    "Usos:",
    knowledge.recordar(
        "python",
        "usos"
    )
)


print(
    "Descripcion nuevamente:",
    knowledge.recordar(
        "python",
        "descripcion"
    )
)


knowledge.guardar(
    "Python",
    "lenguaje de programacion",
    "descripcion"
)


print()
print("Agregar fuente de usuario:")

print(
    knowledge.agregar_fuente(
        "Python",
        "usuario"
    )
)


print()
print("Agregar fuente de Internet:")

print(
    knowledge.agregar_fuente(
        "Python",
        "internet",
        "https://ejemplo.com/python"
    )
)


print()
print("Agregar la misma fuente de Internet nuevamente:")

print(
    knowledge.agregar_fuente(
        "Python",
        "internet",
        "https://ejemplo.com/python"
    )
)


print()
print("Agregar otra fuente de Internet:")

print(
    knowledge.agregar_fuente(
        "Python",
        "internet",
        "https://otro-sitio.com/python"
    )
)
print()
print("Prueba de existencia:")

print(
    "Existe Python:",
    knowledge.existe("Python")
)

print(
    "Existe python:",
    knowledge.existe("python")
)

print(
    "Existe PYTHON:",
    knowledge.existe("PYTHON")
)

print(
    "Existe Java:",
    knowledge.existe("Java")
)