n= soman = total = maior = menor =0
parada=' '
while parada != 'N':
    n=int(input("\033[1mDigite um número:\n ->\033[m"))
    soman += n
    total +=1
    if n > maior:
        maior = n
    else:
        menor = n
    parada=input("\033[3mDeseja adicionar mais número? \033[m\nDigite \033[1;32mS para SIM \033[m ou \033[1;34mN para NÃO?\033[m \n->").upper().strip()
    if parada != 'S' and parada != 'N':
        print ("INVÁLIDO")
print('\n                          FIM - RESULTADOS                                            ')
print ("Foram digitados {} números, a soma é {} e a média é {:.2f}".format(total,soman,(soman/total)))
print ("O menor valor digitado foi {}  e o maior foi {}".format(menor,maior))
