# tests.py
import numpy as np

class PruebaMedia:
    def __init__(self, numeros):
        self.numeros = numeros

    def calcular(self):
        n = len(self.numeros)
        media = np.mean(self.numeros)
        z = (media - 0.5) * np.sqrt(12*n)
        return f"Media = {media:.4f}, Z = {z:.4f}"

class PruebaVarianza:
    def __init__(self, numeros):
        self.numeros = numeros

    def calcular(self):
        n = len(self.numeros)
        varianza = np.var(self.numeros)
        chi = (12*n*varianza - n) / np.sqrt(24*n)
        return f"Varianza = {varianza:.4f}, Chi = {chi:.4f}"

class PruebaChi2:
    def __init__(self, numeros, k=10):
        self.numeros = numeros
        self.k = k

    def calcular(self):
        n = len(self.numeros)
        frec, _ = np.histogram(self.numeros, bins=self.k, range=(0,1))
        esperada = n/self.k
        chi2 = np.sum((frec-esperada)**2 / esperada)
        return f"Chi² = {chi2:.4f} con {self.k-1} gl"
