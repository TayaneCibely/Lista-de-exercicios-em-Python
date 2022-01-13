horas_extras = float(input("Digite o número de horas extras trabalhadas: "))
horas_faltas = float(input("Digite o numeros de horas que faltou ao trabalho: "))

h = horas_extras - 2/3*horas_faltas

if h > 2.400:
    gratificacao = 'R$500,00'
    print("Sua gratificação é de: ",gratificacao)
elif 1.800 <= h <= 2.400:
    gratificacao = 'R$400,00'
    print("Sua gratificação é de: ",gratificacao)
elif 1.200 <= h < 1.800:
    gratificacao = 'R$300,00'
    print("Sua gratificação é de: ",gratificacao)
elif 600 <= h < 1.200:
    gratificacao = 'R$200,00'
    print("Sua gratificação é de: ",gratificacao)
else:
    gratificacao = 'R$100,00'
    print("Sua gratificação é de: ",gratificacao)
