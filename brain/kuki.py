# -*- coding: utf-8 -*-

import json
from datetime import datetime

from brain.learning import Learning
from brain.neuron import Neuron
from brain.memory import Memory
from brain.language import LanguageProcessor



class Kuki:

    def __init__(self):
        self.neurona = Neuron()
        self.memoria = Memory()
        self.aprendizaje = Learning(self.memoria)
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

        # Primero intentamos aprender algo nuevo
        aprendio = self.aprendizaje.aprender_frase(entrada)

        if aprendio:
            return "Lo recordare."

        # Si no aprendio nada, procesamos la intencion
        resultado = self.lenguaje.procesar(entrada)
        intencion = resultado["intencion"]

        if intencion == "saludo":
            return "Hola Agustin. Como estas?"

        elif intencion == "estado":
            return "Estoy funcionando correctamente."

        elif intencion == "nombre":
            return "Mi nombre es KUKI."

        elif intencion == "hora":
            hora_actual = datetime.now().strftime("%H:%M")
            return "Son las " + hora_actual

        elif intencion == "recordar":

            clave = resultado["clave"]
            valor = self.memoria.recordar(clave)

            if valor is not None:
                return "Tu " + clave + " es " + valor + "."

            return "No recuerdo eso todavia."

        else:
            return "Todavia no se como responder a eso."