somaidade = 0
homem = 0
mulheres = 0
media = 0
nomehomem = 'X'
invalido=0
somahomem = 0
somamulher= 0
sexolit =('Y')
for i in range (1,5):
    print ('-----------------------------------------------------------------------')
    print ("DADOS {}".format(i))
    nome = input("Qual seu nome? \n").upper().strip()
    sexo = (int(input("Qual seu sexo? \n \033[1m[1] Masculino \n [2] Feminino \n\033[m")))
    if sexo != 1 and sexo !=2:
        print ("Inválido")
        sexo = 0
    elif sexo == 1:
        sexolit = "masculino"
    elif sexo == 2:
        sexolit = "feminino"
    idade=int(input("Qual sua idade? \n"))
    somaidade = somaidade + idade
    print ('{}, {} anos, sexo {}'.format(nome,idade,sexolit))
    if sexo == 1:
        somahomem +=1
        if idade > homem:
            homem = idade
            nomehomem = nome
    if sexo == 2:
        somamulher +=1
        if idade <= 19:
            mulheres += mulheres + 1
print ('---------------------------------------------------------------------------')
print ("A soma das idades é {} anos, e a média de idades é {}.".format(somaidade,somaidade/4))
if somahomem == 0:
    print ("Não há homens")
else:
    print ("O homem mais velho tem {} anos e se chama {}.".format(homem,nomehomem))
if somamulher == 0:
    print ("Não há mulheres")
else:
    print ("Há {} mulher(es) com menos de 20 anos.".format(mulheres))
