vel=float(input("Qual velocidade você estava?"))
if vel >80:
    print ("Você ultrapassou os limites em {}km e pagará R${:.2f} de multa".format((vel-80),(vel-80)*7))
else:
    print ("Velocidade ok")
print ("FIM!")