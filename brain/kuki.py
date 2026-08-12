# -*- coding: utf-8 -*-

import json
from datetime import datetime

from brain.neuron import Neuron
from brain.memory import Memory
from brain.language import LanguageProcessor



class Kuki:

    def __init__(self):
        self.neurona = Neuron()
        self.memoria = Memory()
        self.lenguaje = LanguageProcessor()

        self.cargar_modelo()

    def cargar_modelo(self):

        with open(
            "models/kuki_neuron.json",
            "r",
            encoding="utf-8"
        ) as archivo:

            modelo = json.load(archivo)

        self.neurona.peso = modelo["peso"]
        self.neurona.bias = modelo["bias"]

        print("Modelo de KUKI cargado.")
        print("Peso:", self.neurona.peso)
        print("Bias:", self.neurona.bias)

    def pensar(self, entrada):

        return self.neurona.predecir(entrada)

    def entender(self, texto):
        return self.lenguaje.procesar(texto)

    def aprender(self, clave, valor):

        self.memoria.guardar(clave, valor)

    def recordar(self, clave):

        return self.memoria.recordar(clave)

    def responder(self, entrada):
        resultado = self.lenguaje.procesar(entrada)
        intencion = resultado["intencion"]

        if intencion == "saludo":
            return "Hola Agustin. Como estas?"

        elif intencion == "estado":
            return "Estoy funcionando correctamente."

        elif intencion == "nombre":
            return "Mi nombre es KUKI."

        if intencion == "hora":
          hora_actual = datetime.now().strftime("%H:%M")
          return "Son las " + hora_actual

        else:
            return "Todavia no se como responder a eso."