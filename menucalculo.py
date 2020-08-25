from time import sleep
n1 = 0
n2 = 0
op = ('')
while op != 5:
    print ('\033[1m*************************\033[m')
    n1=int(input("Digite um número \n -> "))
    n2=int(input("Digite outro número \n -> "))
    print ('\033[1m*************************\033[m')
    print ('\033[1;31m[1] SOMAR \n\033[1;32m[2] MULTIPLICAR \n\033[1;33m[3] MAIOR \n\033[1;34m[4] NOVOS NÚMEROS \n\033[1;35m[5] SAIR \n\033[m')
    op = int(input("Qual operação você quer? \n -> "))
    if op == 1:
        print (' ')
        print ("A soma entre {} e {} é {} ".format(n1,n2,n1+n2))
    elif op == 2:
        print (' ')
        print("A multiplação entre {} e {} é {} ".format(n1, n2, n1 * n2))
    elif op == 3:
        if n1 > n2:
            print (' ')
            print ("O maior número entre {} e {} é {}".format(n1,n2,n1))
        elif n2 > n1:
            print (' ')
            print ("O maior número entre {} e {} é {}".format(n1,n2,n2))
        elif n1==n2:
            print (' ')
            print ("Eles são iguais")
    elif op > 5:
        print ("INVÁLIDO!")
    print ('-------------------')
    print ("Novamente...")
    sleep (1)
    print (' ')
print ("FIM")