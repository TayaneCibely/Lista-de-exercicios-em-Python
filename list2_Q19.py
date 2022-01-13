altura = float(input("Digite sua altura: "))
sexo = int(input("Digite 1-Homem ou 2-Mulher: "))

if sexo==1:
    peso_ideal = (72.5*altura)-58
    print("Seu peso ideal é de: ", peso_ideal)
elif sexo==2:
    peso_ideal = (62.1*altura)-44.7
    print("Seu peso ideal é de: ", peso_ideal)
else:
    print("Opção inválida!")



