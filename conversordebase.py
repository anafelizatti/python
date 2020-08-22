nro=int(input("Digite o número:\n"))
conversor=int(input("Para qual base você deseje converter? \n[1] Binário \n[2] Octal \n[3] Hexadecimal \n-> "))
if conversor ==1:
    print ("O número {} em binário é \033[2;33;44m{}\033[m ".format(nro,bin(nro)[2:])) #o py coloca dois digitos de sinalização, então ao escrever [2:] escolhe-se remover esses dois primeiros.
elif conversor ==2:
    print ("O número {} em octal é \033[2;33;44m{}\033[m".format(nro,oct(nro)[2:]))
elif conversor ==3:
    print("O número {} em hexadecimal é \033[2;33;44m{}\033[m".format(nro,hex(nro)[2:]))
else:
    print ("Seu número é inválido.")
print ("\033[1;32;40mFIM!\033[m")