total = 0
nro = int(input("Digite um número:\n ->"))
for i in range(1, nro + 1):
    if nro % i == 0:
        print('\033[34m', end=' ')
        total += 1
    else:
        print('\033[37m', end=' ')
    print('{}'.format(i), end=' ')
print("\n\033[mO número {} foi divisível {} vezes".format(nro, total))
if total >= 3:
    print ("O número {} não é um número primo.".format(nro))
else:
    print ("É um número primo.")


