n1=float(input('Digite um número: '))
n2=float(input('Digite outro número: '))
if n1>n2:
    print ('O maior número é \033[2;30;41m{}\033[m'.format(n1))
elif n1<n2:
    print ('O maior número é \033[2;30;42m{}\033[m'.format(n2))
else:
    print ("Os números são \033[1miguais\033[m")
