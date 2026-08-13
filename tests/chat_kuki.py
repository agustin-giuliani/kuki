from brain.kuki import Kuki


kuki = Kuki()

print()
print("================================")
print("       KUKI - CONSOLA")
print("================================")
print("Escribi 'salir' para terminar.")
print()


while True:

    entrada = input("Vos: ")

    if entrada.lower().strip() == "salir":
        print("KUKI: Hasta luego, Agustin.")
        break

    respuesta = kuki.responder(entrada)

    print("KUKI:", respuesta)
