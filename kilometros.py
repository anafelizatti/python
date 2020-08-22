km=float(input("Quantos km você irá viajar? "))
if km <= 200:
    print ("Sua viagem ficará R${:.2f}".format (km*0.5))
else:
    print ("Sua viagem ficará R${:.2f}".format (km*0.45))
print ("Boa viagem")

#outra forma de fazer:
#valor = km*0.5 if km <= 200 else km*0.45