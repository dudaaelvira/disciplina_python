numero=float(input("digite um número: "))
#print("{}".format(numero))
#numero2 =numero-1
#print("{}".format(numero2))
#numero3 =(numero-1)-1
#print("{}".format(numero3))
total = 1

while numero != 0:
    total = total * numero
    numero = numero - 1

print(total)
