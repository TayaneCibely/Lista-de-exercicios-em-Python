salario = float(input("Digite o valor do seu salário: "))

if salario < 300:
    novo_salario = salario * 135/100
    print("Parabéns você recebeu um aumento, seu novo salário é: ", novo_salario)
else:
    novo_salario = salario * 115/100
    print("Parabéns você recebeu um aumento, seu novo salário é: ", novo_salario)
