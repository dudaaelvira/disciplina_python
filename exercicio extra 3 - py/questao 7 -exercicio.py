contador = 0
maior_peso = 0
maior_altura = 0
nome_maior_peso = ""
nome_maior_altura = ""

while contador < 10:
    contador = contador + 1

    nome_atual = str(input("digite o seu nome:"))
    altura_atual = float(input("digite a sua altura:"))
    peso_atual = float(input("digite o seu peso:"))
    
    if peso_atual > maior_peso:
        maior_peso = peso_atual
        nome_maior_peso = nome_atual


    if altura_atual > maior_altura:
        maior_altura = altura_atual
        nome_maior_altura = nome_atual


print("{} é a pessoa mais pesada com {} Kg".format(nome_maior_peso,maior_peso))
print("{} é a pessoa mais alta com {} m".format(nome_maior_altura,maior_altura))
