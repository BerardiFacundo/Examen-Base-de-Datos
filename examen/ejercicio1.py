alumnos = ["Alan B", "Luca Lopez", "Camila Ricardo", "Facundo Berardi", "Matias Celiz", "Tomas Dimauro", "Nataly Sado", "Dorrego juan"]

import random

notas = {}

for alumno in alumnos:
  notas[alumno] = [random.randint(1, 10) for _ in range(6)]

print("\nDiccionario completo de notas:")
for alumno, notas_alumno in notas.items():
    print(f"{alumno}: {notas_alumno}")

print("\nPromedio de alumnos")
for alumno, calificaciones in notas.items():

  promedio = sum(calificaciones) / len(calificaciones)

  print( f"{alumno}: {promedio:.2f}")