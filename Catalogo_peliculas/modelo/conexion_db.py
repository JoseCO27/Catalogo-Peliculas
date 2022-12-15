import sqlite3

# Conexión de la BD
class ConexionDB:
    def __init__(self):
        self.base_datos = 'database/peliculas.db'
        self.conexion = sqlite3.connect(self.base_datos)
        # Para ejecutr sql dentro de la bd
        self.cursor = self.conexion.cursor()
    
    def cerrar (self):
        self.conexion.commit()
        self.conexion.close()