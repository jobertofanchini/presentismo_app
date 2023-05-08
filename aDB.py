import sqlite3


conexion = sqlite3.connect(".\\data\\comision22918.db")
cursor = conexion.cursor()

conexion.execute("""
                 CREATE TABLE IF NOT EXISTS Alumnos (
                     DNI INTEGER PRIMARY KEY,
                     Apellido TEXT,
                     Nombre TEXT,
                     Teléfono INTEGER,
                     Correo Electrónico TEXT)
                """)


conexion.close()
