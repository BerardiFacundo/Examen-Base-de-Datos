print("Ingresá las notas (del 1 al 10). Para terminar, poné 0\n")

notas_cargadas = []

while True:
   try:
       nota = float(input("Nota: "))
       
       if nota == 0:
           break
           
       if nota < 1 or nota > 10:
           print("Ojo! La nota tiene que ser entre 1 y 10")
           continue
           
       notas_cargadas.append(nota)
       
   except:
       print("Por favor ingresá un número válido")

if notas_cargadas:
   print("\nLista completa de notas:")
   print(f"\nNotas cargadas: {notas_cargadas}")
   print("\nResumen de notas:")
   print(f"Nota más alta: {max(notas_cargadas)}")
   print(f"Nota más baja: {min(notas_cargadas)}")
   print(f"Promedio del curso: {sum(notas_cargadas)/len(notas_cargadas):.2f}")
   
else:
   print("No se cargaron notas")