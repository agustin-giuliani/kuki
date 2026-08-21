from brain.conversation import Conversation
from brain.context import ContextManager


conversacion = Conversation(
    "data/test_context_conversation.json"
)

contexto = ContextManager(
    conversacion
)


print("--- CONTEXT MANAGER ---")


print()
print("Tema inicial:")

print(
    contexto.obtener_tema()
)


print()
print("Procesar Python:")

resultado_python = contexto.procesar({
    "intencion": "conocimiento",
    "clave": "python"
})

print(
    resultado_python
)


print()
print("Tema actual:")

print(
    contexto.obtener_tema()
)


print()
print("Pregunta contextual:")

resultado_contextual = contexto.procesar({
    "intencion": "pregunta_contextual"
})

print(
    resultado_contextual
)


print()
print("Tema despues de pregunta:")

print(
    contexto.obtener_tema()
)


print()
print("Procesar Blender:")

resultado_blender = contexto.procesar({
    "intencion": "conocimiento",
    "clave": "blender"
})

print(
    resultado_blender
)


print()
print("Tema final:")

print(
    contexto.obtener_tema()
)