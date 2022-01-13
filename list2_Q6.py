n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))

print("\nMenu")
print("1-Calcular a média: ")
print("2-Calcular a diferença do maior pelo menor: ")
print("3-Calcular  o produto: ")

op = int(input())

if op==1:
    med = (n1+n2)/2
    print("O resultado é: ",med)
elif op==2:
    if n1>n2:
        sub = n1-n2
    else:
        sub = n2-n1
    print("A diferença é: ",sub)
elif op==3:
    pro = n1*n2
    print("O Resultado da multiplicaçao é: ", pro)
else:
    print("Erro! Opção inválida!")
         
