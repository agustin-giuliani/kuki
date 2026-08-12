from neuron import Neuron


# Creamos nuestra primera neurona
neurona = Neuron()

entrada = 1
objetivo = 1

print("Entrenando KUKI...\n")

for epoca in range(10):
    salida, error = neurona.entrenar(
        entrada,
        objetivo,
        tasa_aprendizaje=0.1
    )

    print(
        "Epoca:", epoca + 1,
        "| Salida:", salida,
        "| Error:", error,
        "| Peso:", neurona.peso,
        "| Bias:", neurona.bias
    )


