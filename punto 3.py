# tercer punto
n = int(input("Ingrese la base (máximo 9): "))
x = int(input("Ingrese el exponente máximo (máximo 9): "))
if n > 9 or x > 9:
    print("Valores fuera del rango permitido")
else:
    i = 0
    print("Potencias de", n, "hasta el exponente", x, ":")
    while i <= x:
        print(n**i)
        i += 1

