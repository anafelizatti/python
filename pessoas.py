from datetime import date
maior=0
menor=0
for i in range (1,7):
    ano=int(input("ANO {} \n->".format(i)))
    if ano > 2020 or ano < 1500:
        print ("Não é um ano válido")
    else:
        idade = date.today().year - ano
        print ('{} anos de idade'.format(idade))
        if idade > 18:
            maior += 1
        else:
            menor += 1
print (' ')
print ("Há {} pessoas maiores de idade e {} menores de idade".format(maior,menor))

