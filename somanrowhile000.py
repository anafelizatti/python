'''total = nro = ndigitados= 0
while nro != 999:
    nro=int(input("Digite um número\n->:"))
    total += nro
    ndigitados +=1
print ("Foram digitados {} números, e a soma é {}".format(ndigitados-1,total-999))'''

#ou
total = nro = ndigitados= 0
nro=int(input("Digite um número\n->:")) # trocando o flag de lugar para evitar que some o 999
while nro != 999:
    total += nro
    ndigitados +=1
    nro = int(input("Digite um número\n->:"))
print ("Foram digitados {} números, e a soma é {}".format(ndigitados,total))
