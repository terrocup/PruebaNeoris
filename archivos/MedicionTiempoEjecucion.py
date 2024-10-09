# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 08:30:53 2024

@author: LCardenas
"""
from math import sqrt
import time

def cuadrado(n:int):
    return n*n
def raiz(m:int):
    return sqrt(m)

print(raiz(cuadrado(5)))

def timing_decorator(funcion):
    inicio = time.time()
    funcion
    final = time.time()
    return(inicio - final)
timing_decorator(cuadrado(5))
timing_decorator(raiz(25))