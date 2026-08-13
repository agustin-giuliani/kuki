from brain.conversation import Conversation
from brain.context import ContextManager


conversacion = Conversation()
contexto = ContextManager(conversacion)

print("--- CONTEXTO DE KUKI ---")

datos = contexto.obtener_contexto(4)

for mensaje in datos["mensajes"]:

    print(
        mensaje["rol"] + ":",
        mensaje["mensaje"]
    )

print()
print("--- DETECCION AUTOMATICA ---")

resultado = {
    "intencion": "conocimiento",
    "clave": "python"
}

tema = contexto.actualizar_tema(resultado)

print("Tema detectado:", tema)