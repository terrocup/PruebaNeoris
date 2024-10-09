# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 12:05:04 2024

@author: LCardenas
"""


import asyncio
import pandas as pd

async def sumarvalores(archivo):
    df2=pd.read_csv(archivo)
    suma = await df2['value'].sum()
    return(suma)
async def main():
    batch = asyncio.gather(sumarvalores("Primercsv.csv"), sumarvalores("Segundocsv.csv"), sumarvalores("Tercercsv.csv"))
    sumaprimero, sumasegundo, sumatercero = await batch
    print(f"La suma del primer archivo es: {sumaprimero}")
    print(f"La suma del segundo archivo es: {sumasegundo}")
    print(f"La suma del tercer archivo es: {sumatercero}")

if __name__ == "__main__":
    asyncio.run(main())


