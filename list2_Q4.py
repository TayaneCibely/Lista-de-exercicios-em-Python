a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))

if a>b>c:
    print("O maior número é: ",a)
elif b>a>c:
    print("O maior número é: ",b)
elif c>a>b:
    print("O maior número é: ",c)
elif a>c>b:
    print("O maior número é: ",a)
elif b>c>a:
    print("O maior número é: ",b)
elif c>b>a:
    print("O maior número é: ",c)
