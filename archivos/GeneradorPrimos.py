# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 07:32:23 2024

@author: LCardenas
"""



def prime_sequence_generaror(n:int):
    primos = []
    for numero in range(n + 1):
       # all prime numbers are greater than 1
       if numero > 1:
           for i in range(2, numero):
               if (numero % i) == 0:
                   break
           else:
               primos.append(numero)
    return primos
print(prime_sequence_generaror(125))