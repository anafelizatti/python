answer="S"
while answer == "S":
    nro = int(input("Digite um número \n -> "))
    answer = str(input("QUER CONTINUAR? [S] ou [N] \n-> ")).upper().strip()
if answer != "S" and answer != 'N':
    print ("\033[1mINVÁLIDO!\033[m")
print ("FIM")


