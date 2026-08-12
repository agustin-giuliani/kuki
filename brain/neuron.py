class Neuron:
    def __init__(self, peso=0.5, bias=0.0):
        self.peso = peso
        self.bias = bias
    
    def predecir(self, entrada):
        return entrada * self.peso + self.bias
    
    def activar(self, entrada):
        return (entrada * self.peso) + self.bias

    def entrenar(self, entrada, objetivo, tasa_aprendizaje=0.1):
        salida = self.activar(entrada)

        error = objetivo - salida

        self.peso += tasa_aprendizaje * error * entrada
        self.bias += tasa_aprendizaje * error

        return salida, error

