# segundo punto
notas = []
cantidad = int(input("Ingrese la cantidad de notas: "))
i = 0
while i < cantidad:
    nota = float(input(f"Ingrese la nota {i+1}: "))
    notas.append(nota)
    i += 1
suma = 0
contador = 0
i = 0
while i < len(notas):
    suma += notas[i]
    contador += 1
    i += 1
if contador > 0:
    print("El promedio de notas es:", suma / contador)
else:
    print("No se ingresaron notas")

