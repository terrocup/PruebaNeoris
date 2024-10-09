# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 13:26:19 2024

@author: LCardenas
"""

import pytest

def espalindroma(a: str):
    a = a.lower()
    if a == a[::-1]:
        return True
    else:
        return False

cadena = "Anilina"
print(espalindroma(cadena))

def Prueba1():
    assert espalindroma("murcielago") == False
    
def Prueba2():
    assert espalindroma("Anilina") == True