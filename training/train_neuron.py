from brain.neuron import Neuron
from data.training_data import entradas, objetivos

# Creamos la neurona
neurona = Neuron()

# Cantidad de veces que recorreremos los datos
epocas = 100

print("Entrenando KUKI...\n")

for epoca in range(epocas):

    error_total = 0.0

    # Recorremos todos los ejemplos
    for entrada, objetivo in zip(entradas, objetivos):

        salida, error = neurona.entrenar(
            entrada,
            objetivo,
            tasa_aprendizaje=0.01
        )

        error_total += abs(error)

    # Mostramos información cada 10 épocas
    if epoca % 10 == 0:
        print(
            "Epoca:", epoca,
            "| Error total:", error_total,
            "| Peso:", neurona.peso,
            "| Bias:", neurona.bias
        )

print("\nEntrenamiento terminado.")
print("Peso final:", neurona.peso)
print("Bias final:", neurona.bias)

# Guardamos el modelo entrenado
import json

modelo = {
    "peso": neurona.peso,
    "bias": neurona.bias
}

with open("models/kuki_neuron.json", "w") as archivo:
    json.dump(modelo, archivo, indent=4)

print("Modelo guardado correctamente.")
