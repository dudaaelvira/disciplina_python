salario= float(input("digite o seu salário: "))
#aumento= (salario*0.15)+salario
if salario<1500:
    salarioatual= (salario*0.15)+salario
    print("O seu salário com o acréscimo de 15% é de: {}".format(salarioatual))
elif salario>= 1500 and salario<1750:
    salarioatual= (salario*0.12)+salario
    print("O seu salário com o acréscimo de 12% é de: {}".format(salarioatual))
elif salario>= 1750 and salario<2000:
    salarioatual= (salario*0.10)+salario
    print("O seu salário com o acréscimo de 10% é de: {}".format(salarioatual))
elif salario>= 1750 and salario<2000:
    salarioatual= (salario*0.10)+salario
    print("O seu salário com o acréscimo de 10% é de: {}".format(salarioatual))
elif salario>= 2000 and salario<3000:
    salarioatual= (salario*0.07)+salario
    print("O seu salário com o acréscimo de 7% é de: {}".format(salarioatual))
elif salario>= 3000: 
    salarioatual= (salario*0.05)+salario
    print("O seu salário com o acréscimo de 5% é de: {}".format(salarioatual))


