#  1. primer punto
a = int(input("ingrese el primer numero: "))
b = int(input("ingrese el segundo numero: "))
resultado = 0
c = abs(b)
while c > 0:
    resultado += abs(a)
    c -= 1
if (a > 0 and b > 0) or (a < 0 and b < 0):
    print("resultado de la multiplicacion:" , resultado)
else:
    print("resultado de la multiplicacion:" , -resultado)
    
