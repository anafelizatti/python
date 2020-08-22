peso=float(input("Qual seu peso? "))
altura=float(input("Qual sua altura em metros? "))
IMC = (peso/(altura**2))
print ('{:.2f}'.format(IMC))
if IMC < 18.5:
    print ("Você está abaixo do peso.")
elif 18.5 <= IMC < 25:
    print ("Você está no peso ideal.")
elif 25 <= IMC < 30:
    print("Você está com sobrepeso.")
elif 30 <= IMC < 40:
    print("Você está com obesidade.")
elif IMC > 40:
    print("Você está com obesidade mórbida.")
