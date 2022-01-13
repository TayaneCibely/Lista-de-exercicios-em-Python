print("Tipos de investimento")
print("1-Poupança")
print("2-Fundos de Renda Fixa")

op = int(input())

valor_invest = float(input("Digite o valor a ser investido: "))

if op==1:
    renda = valor_invest*103/100
    print("O rendimento mensal do valor investido é: ",renda)
elif op==2:
    renda = valor_invest*104/100
    print("O rendimento mensal do valor investido é: ",renda)
else:
    print("Opção inválida!")   
        
    
