par=0
impar=0
nro=1
while nro != 0:
    nro=int(input("Digite um número:\n->"))
    if nro !=0:
        if nro % 2 == 0:
            par += 1
        else:
            impar += 1
print ("FIM")
print ("Dentre os valores digitados, {} são pares e {} são ímpares.".format(par,impar))