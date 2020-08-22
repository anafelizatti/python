soma = 0
n: int
for n in range (1,501):
    if n % 2 != 0 and n % 3 == 0:
        print ('Número impar:{}'.format(n))
        soma += n
        print ("\033[1mSoma: {}\033[m".format(soma))

print ('Soma total: \033[1;30;45m{}\033[m'.format(soma))