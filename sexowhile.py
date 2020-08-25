'''sexo = ' '
while sexo != "F" and sexo != "M":
    sexo = str(input("QUAL SEU SEXO? F OU M?")).upper().strip()
    if sexo == "F":
        print ("Olá, seu sexo é feminino")
    if sexo == "M":
        print ("Olá, seu sexo é masculino")
print ("FIM")'''

sexo=str(input('Qual seu sexo, Masculino ou Feminino?')).upper().strip()[0]#pegar só a primeira letra)
while sexo not in 'MF':
    sexo =str(input("Inválido. Digite seu sexo: M/F")).upper().strip()[0]
print (sexo)

