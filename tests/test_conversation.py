from brain.conversation import Conversation


conversacion = Conversation()

print("--- HISTORIAL RECIENTE DE KUKI ---")

historial = conversacion.obtener_recientes(4)

for mensaje in historial:

    print(
        mensaje["rol"] + ":",
        mensaje["mensaje"]
    )

print()
print("--- ULTIMO MENSAJE DEL USUARIO ---")

ultimo = conversacion.obtener_ultimo_usuario()

print("Usuario:", ultimo)