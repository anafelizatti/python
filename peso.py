menor = 0
maior = 0
for i in range (1,6):
    peso=float(input('Qual o peso {} em kg ? '.format(i) ))
    print ("\033[1mPeso {} = {}kg\033[m".format(i,peso))
    if i == 1:
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('---'*20)
print ("O menor peso foi \033[1m{}kg\033[m e o maior peso foi \033[1m{}kg\033[m".format(menor,maior))


