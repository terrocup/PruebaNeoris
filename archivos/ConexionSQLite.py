# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 14:11:13 2024

@author: LCardenas
"""
import sqlite3

class conexion:
    
    def __init__(self, url):
        self.url = url

    def conectar(self):
        conn = sqlite3.connect(self.url)
        print("Se a conectado a la base de datos: ", self.url)
        return conn
    
    def correrconsulta(conn, consulta):
        cursor = conn.cursor()
        cursor.excecute(consulta)
        conn.commit
        cursor.close()
    def desconectar(self, conn):
        conn.close()
        print("la conexion ", self.url, " se ha desconectado")
        
conexion1 = conexion("sqlite/PruebaDB.db")
conn1 = conexion1.conectar()
conexion1.correrconsulta(conn1, "CREATE TABLE IF NOT EXISTS contacts (contact_id INTEGER PRIMARY KEY,first_name TEXT NOT NULL, last_name TEXT NOT NULL, email TEXT NOT NULL UNIQUE, phone TEXT NOT NULL UNIQUE);")
conexion1.desconectar(conn1)