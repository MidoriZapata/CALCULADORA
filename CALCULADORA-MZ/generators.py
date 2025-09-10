# generators.py
import numpy as np

class CuadradosMedios:
    def __init__(self, seed, n):
        self.seed = seed
        self.n = n

    def generar(self):
        nums = []
        x = self.seed
        for _ in range(self.n):
            x = int(str(x**2).zfill(8)[2:6])  # extraer cifras del medio
            nums.append(x / 10000)  # normalizado 0-1
        return nums


class ProductosMedios:
    def __init__(self, seed1, seed2, n):
        self.x = seed1
        self.y = seed2
        self.n = n

    def generar(self):
        nums = []
        for _ in range(self.n):
            p = str(self.x * self.y).zfill(8)
            self.x, self.y = self.y, int(p[2:6])
            nums.append(self.y / 10000)  # normalizado 0-1
        return nums


class MultiplicadorConstante:
    def __init__(self, seed, n, a):
        """
        seed: semilla inicial
        n: cantidad de números a generar
        a: constante multiplicativa
        """
        self.x = seed
        self.n = n
        self.a = a

    def generar(self):
        nums = []
        x = self.x  # usar variable local para no modificar la semilla original
        for _ in range(self.n):
            x = (self.a * x) % 10000
            nums.append(x / 10000)  # normalizado 0-1
        return nums
