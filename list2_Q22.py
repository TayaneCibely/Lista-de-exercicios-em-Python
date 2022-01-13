idade = int(input("Digite sua idade: "))
peso = float(inpu("Digite seu peso: "))

if idade < 20:
    if peso <= 60:
        print("Risco 9")
    elif 60 < peso <= 90:
        print("Risco 8"
    else:
        print("Risco 7")
elif 20 < idade <=50:
    if peso <= 60:
        print("Risco 6")
    elif 60 < peso <= 90:
        print("Risco 5"
    else:
        print("Risco 4")
else:
    if peso <= 60:
        print("Risco 3")
    elif 60 < peso <= 90:
        print("Risco 2"
    else:
        print("Risco 1")         

    
