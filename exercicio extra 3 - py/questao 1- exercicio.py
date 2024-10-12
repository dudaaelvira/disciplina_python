nome1= str(input("digite o seu nome: "))
peso1= float(input("digite o seu peso: "))
altura1= float(input("digite sua altura: "))
nome2= str(input("digite o seu nome: "))
peso2= float(input("digite o seu peso: "))
altura2= float(input("digite sua altura: "))
if altura1>altura2 and peso1>peso2:
    print("A pesssoa mais alta e com maior peso é: {}".format(nome1))
elif altura2>altura1 and peso2>peso1:
    print("A pessoa mais alta e com maior peso é: {}".format(nome2))
elif altura2>altura1 and peso1>peso2:
    print("A pessoa mais alta é: {}, e a pessoa com maior peso é: {}".format(nome2,nome1))
elif altura1>altura2 and peso2>peso1:
    print("A pessoa mais alta é: {}, e a pessoa com maior peso é: {}".format(nome1,nome2))
