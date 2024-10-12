''' faça um algorítimo que leia um numero inteiro e mostre uma mensagem
indicando se este numero é par ou impar e se é positivo ou negativo'''

numero= int(input("digite um número inteiro: "))
if numero % 2 == 0:
    print("O número {} é par".format(numero))
else:
    print("O número {} é ímpar".format(numero))

if numero > 0:
    print("O número {} é positivo".format(numero))
else:
    print("O número {} é negativo".format(numero))
