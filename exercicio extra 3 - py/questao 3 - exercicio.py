salario= float(input("digite o seu salário: "))
desconto= salario*0.11
salarioatual= salario-desconto
if desconto<=318.20:
    print("o valor do seu desconto é: {}".format(desconto))
elif desconto>318.20:
    print("o valor do seu desconto é 318,20")
