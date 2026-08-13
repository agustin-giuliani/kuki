from brain.kuki import Kuki


print("--- KUKI ---")

kuki = Kuki()

print("\n--- PREDICCIONES ---")

entradas = [0, 1, 2, 3, 4, 5, 10]

for entrada in entradas:

    prediccion = kuki.pensar(entrada)

    print(
        "Entrada:", entrada,
        "| KUKI piensa:", prediccion
    )

print("\n--- MEMORIA ---")

kuki.aprender("nombre", "Agustin")

print("KUKI aprendio el nombre.")

nombre = kuki.recordar("nombre")

print("KUKI recuerda:", nombre)

print("\n--- CONVERSACION ---")

print("Usuario: Hola KUKI")
print("KUKI:", kuki.responder("Hola KUKI"))

print("Usuario: Como estas")
print("KUKI:", kuki.responder("Como estas"))

print("Usuario: Cual es tu nombre")
print("KUKI:", kuki.responder("Cual es tu nombre"))

print("Usuario: Que hora es")
print("KUKI:", kuki.responder("Que hora es"))

print("Usuario: Mi comida favorita es la pizza")
print("KUKI:", kuki.responder("Mi comida favorita es la pizza"))

print("Usuario: Cual es mi comida favorita?")
print("KUKI:", kuki.responder("Cual es mi comida favorita?"))