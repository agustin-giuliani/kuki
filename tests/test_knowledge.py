from brain.knowledge import Knowledge


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
    knowledge.recordar("python", "usos")
)

print(
    "Descripcion nuevamente:",
    knowledge.recordar("python", "descripcion")
)