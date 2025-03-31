# quinto punto
n = int(input("Ingrese un número para calcular su factorial (entre 0 y 20): "))
if n < 0 or n > 20:
    print("Número fuera del rango permitido")
else:
    resultado = 1
    i = 1
    while i <= n:
        resultado *= i
        i += 1
    print("El factorial de", n, "es:", resultado)

