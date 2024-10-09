# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 17:17:30 2024

@author: LCardenas
"""

from multiprocessing import Pool

def contar_palabras(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            palabras = contenido.split()
            conteo_palabras = len(palabras)
            return conteo_palabras
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró.")
        return 0
    
articulos = ["Gago.txt", "Checo.txt", "Jets.txt"] 

if __name__ == '__main__':
    with Pool(5) as p:
        conteo = p.map(contar_palabras, articulos)
print(conteo)


diccionario = dict(zip(articulos, conteo))
print(diccionario)