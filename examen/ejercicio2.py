import sqlite3

conexion = sqlite3.connect('EESTN5.db')
cursor = conexion.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS alumnos (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        edad INTEGER
    )
''')

datos_alumnos = [
    ("Alan B", 19),
    ("Luca Lopez", 18),
    ("Camila Ricardo", 17),
    ("Facundo Berardi", 18),
    ("Matias Celiz", 19),
    ("Tomas Dimauro", 19),
    ("Nataly Sado", 40),
    ("Dorrego juan", 5)
]

cursor.executemany("INSERT INTO alumnos (nombre, edad) VALUES (?, ?)", datos_alumnos)

print("\nEstudiantes mayores de 17:")
mayores = cursor.execute("SELECT nombre, edad FROM alumnos WHERE edad > 17")
for estudiante in mayores:
    print(f"{estudiante[0]} - {estudiante[1]} años")

conexion.commit()
conexion.close()