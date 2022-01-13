a = float(input("Digite um número: "))
b = float(input("Digite outro número: "))

print("Menu")
print("1-Calcular a média")
print("2-Subtraçãodo maior pelo menor ")
print("3-Multipliacação")
print("4-Divisão do primeiro pelo segundo ")
     

op = int(input())

if op==1:
      med = (a+b)/2
      print("O resultado da média é: ",med)
elif op==2:
      if a > b:
          sub = a-b
      else:
          sub = b-a
      print("o resultado da subtraçao é: ", sub)
elif op== 3:
      mul = a*b
      print("O resultado da multiplicação é: ", mul)
elif op==4:
      if a==0:
          print("Operação inválida! Não é possível divisão por zero!")
      else:
          div = a/b
      print("O resultado da divisão é: ", div)
else:
    print("Essa opção não existe, tente de novo.")
 
      
      
