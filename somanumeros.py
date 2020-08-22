soma =0
for i in range (0,6):
    nro= int(input('Digite um número:\n'))
    if nro % 2 == 0:
        print ("{} é par!".format(nro))
        soma += nro
    else:
        print("{} é impar!".format(nro))
print ('A soma dos pares digitados é {}'.format(soma))

